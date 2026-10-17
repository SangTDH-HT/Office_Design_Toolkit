---
name: google-fonts-thieu-dau-tieng-viet
description: "Tải font từ fonts.googleapis.com ra bản latin rút gọn ~280 glyph, thiếu sạch dấu tiếng Việt"
---

> Nguồn: ghi nhớ `google-fonts-thieu-dau-tieng-viet`. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Lấy file `.ttf` theo đường dẫn trong CSS của `fonts.googleapis.com` sẽ ra **bản subset
latin ~280 glyph, không có ế ộ ữ ơ Đ ị ẩ ỹ ă**. Chữ tiếng Việt ra ô vuông.

Muốn bản đầy đủ thì tải thẳng từ GitHub repo `google/fonts`, ví dụ
`https://github.com/google/fonts/raw/main/ofl/<tenfont>/<TenFont>-Regular.ttf`.

**Be Vietnam Pro** (527 glyph) là lựa chọn tốt cho phần mềm tiếng Việt — do người Việt
thiết kế riêng, dấu cân đối, có đủ 5 độ đậm Regular/Medium/SemiBold/Bold/ExtraBold.

Kiểm tra trước khi dùng, đừng tin tên file:
```powershell
$fam=[System.Windows.Media.Fonts]::GetFontFamilies("file:///.../x.ttf")|select -First 1
$gt=$null; ($fam.GetTypefaces()|select -First 1).TryGetGlyphTypeface([ref]$gt)
'ằếộữơĐ'.ToCharArray()|?{ -not $gt.CharacterToGlyphMap.ContainsKey([int]$_) }
```
