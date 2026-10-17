---
name: word-seq-caption-field
description: "Chèn caption có field SEQ trong Word COM - phải đặt chỗ trước rồi thay, không append sau"
---

> Nguồn: ghi nhớ `word-seq-caption-field`, cập nhật 2026-08-13. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Caption trong `D:\Du_An_Tot_Nghiep_Thang_May\File_Bao_Cao\Báo cáo tốt nghiệp.docx` là `Hình <SEQ HINHVE \* ARABIC>: <nội dung>`, và danh mục hình là field `TOC \h \z \c "HINHVE"`. Nhờ vậy chèn hình mới **không cần đánh số lại** — chỉ cần `Fields.Update()` + `TablesOfContents/TablesOfFigures.Update()` hai lượt.

Cạm bẫy: đừng `Fields.Add()` trước rồi `InsertAfter(': nội dung')` tại `$f.Result.End`. Chữ đó nằm **bên trong result range của field**, nên `Fields.Update()` kế tiếp xoá sạch — caption chỉ còn "Hình 42".

Cách đúng: ghi cả câu với ký tự thế chỗ, rồi thay đúng 1 ký tự đó bằng field (Fields.Add trên range không rỗng sẽ thay thế range):

```powershell
$r.InsertAfter('Hình ' + '@: ' + $text)
$at = $s + 5                      # vị trí ký tự '@'
$mark = $doc.Range($at, $at + 1)
if ($mark.Text -ne '@') { throw 'lệch vị trí' }   # assert, đừng tin offset suông
[void]$doc.Fields.Add($mark, 12, 'HINHVE \* ARABIC', $true)
```

Hai cạm bẫy nữa khi sửa caption bằng Word COM trên file này:

- **`Range.Find` không tự tiến**: lặp `doc.Range(pos, end)` rồi `Find.Execute()` vẫn trả về **đúng lần trúng đầu tiên** mãi mãi, kể cả khi `Wrap=0`. Mà lần trúng đầu tiên của một câu caption luôn là **mục trong DANH MỤC HÌNH ẢNH** (style `Table of Figures`), không phải caption thật. Cách chắc ăn: tìm **ngược** — `Find.Forward = False` trên `doc.Content` — vì caption thân bài luôn nằm sau mục danh mục.
- **Sửa chữ sau field**: `doc.Range(fld.Result.End, para.End-1).Text = ...` ném `The range cannot be deleted`. Phải bắt đầu từ `fld.Result.End + 2` (bỏ qua ký tự kết field), và nhớ giữ lại dấu cách sau dấu hai chấm.

Xem thêm [word-com-docx-gotchas](word-com-bay.md) và [ps51-utf8-script-encoding](ps51-utf8-tieng-viet.md).
