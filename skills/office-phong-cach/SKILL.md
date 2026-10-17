---
name: office-phong-cach
description: Phong cách và cách làm file Microsoft Office của Sáng — Word (.docx) qua COM PowerShell hoặc sửa XML, form KHBD lề 2-2-3-2 Times New Roman 14 giãn 1,2, báo cáo có mục lục và chú thích hình SEQ, Excel (.xlsx) kiểm công thức bằng Excel thật, file mẫu báo cáo, sửa workbook xuất từ phần mềm khác, PowerPoint (.pptx) qua ppt-master; kèm các bẫy script tiếng Việt trên Windows (BOM, PowerShell 5.1, CRLF, heredoc, bộ gõ). Dùng khi sửa/dựng file Word, Excel, PowerPoint, "căn lề như hôm bữa", "form như hôm trước", "chèn hình đánh số", "làm mục lục", "file bị khoá", "script Word/Excel COM lỗi chữ".
---

# Office theo kiểu Sáng

Skill Anthropic `docx` / `xlsx` / `pptx` lo phần kỹ thuật định dạng file; skill này giữ **khuôn Sáng đã duyệt** và **bẫy đã trả giá trên máy này**. Hai cái dùng cùng nhau.

## Trước khi đụng file

1. File đang mở trong Word/Excel → không `Stop-Process`. Báo tiến trình đang giữ, sửa **bản sao** trong scratchpad rồi chép đè; giữ bản gốc `- ban goc.docx` hoặc `.bak-before-<việc>` cạnh file. → [file-office-bi-khoa](references/file-office-bi-khoa.md)
2. Có mẫu thì đọc mẫu, không đọc trí nhớ: "như hôm bữa / form như hôm trước" = mở đúng file mẫu Sáng chỉ, đo lề/bảng/giãn dòng từ XML của nó.
3. Kiểm kết quả bằng chính Office: Word xuất PDF rồi render PNG (PyMuPDF) + so chữ; Excel cho chính Excel tính công thức qua COM. XML hợp lệ không có nghĩa là bố cục đúng.

## Word

| Khuôn | Thông số chốt | Chi tiết |
|---|---|---|
| Kế hoạch bài dạy (KHBD lớp 1D) | A4, lề trên 2 / dưới 2 / trái 3 / phải 2 cm (NĐ 30/2020); Times New Roman mọi run, cỡ 14 (bảng lịch 12); giãn dòng 1,2 (line=288), after 0; thụt đầu dòng 1 cm; mỗi bài một bảng 2 cột 4536/4536, viền xám `7F7F7F`, không tô nền | [word-form-khbd](references/word-form-khbd.md) |
| Báo cáo dài (đồ án, tốt nghiệp) | Caption `Hình <SEQ HINHVE \* ARABIC>: nội dung`; danh mục hình `TOC \h \z \c "HINHVE"`; mục lục `TOC \o "1-3" \h`; style Normal phải là body text | [word-caption-seq](references/word-caption-seq.md), [word-com-bay](references/word-com-bay.md) |
| Bài làm nộp thầy | Times New Roman 13, chữ đen, không hộp màu — dựng bằng HTML → PDF | skill `tai-lieu-pdf` |

Cách làm đã chạy được:
- **COM từ PowerShell** cho thao tác có field (TOC, SEQ, cập nhật mục lục). Duyệt `foreach ($p in $doc.Paragraphs)` một lần; `Paragraphs.Item($i)` trong vòng lặp là O(n²).
- **Sửa thẳng `word/document.xml`** (lxml/ElementTree trên bản sao) khi phải cắt/xoá hàng trăm đoạn hay chép nguyên `tblPr/tcPr` của bảng mẫu. Hợp nhất `xmlns` của thẻ gốc, đừng ghi đè.
- Chữ append sau `Fields.Add` nằm trong result của field và bị xoá ở lần `Update()` — ghi cả câu với ký tự thế chỗ rồi thay đúng ký tự đó bằng field.
- Đoạn mới thừa hưởng viền/màu/giãn chữ của đoạn trước: xoá `Borders`, `Font.Color`, `Font.Spacing` trên range vừa thêm. Bảng chèn sau Heading kéo cả bảng vào mục lục: đặt `$tbl.Range.Style = Normal`.
- Chữ xanh `1F4E79` trong mẫu KHBD đổi đen; chữ đỏ tích hợp giữ nguyên.

## Excel

- Công thức trong tài liệu (ôn thi, bảng tính kỹ thuật) phải cho **Excel thật** tính qua COM rồi mới ghi đáp số — không tin đáp án trên mạng.
- Sửa workbook có sẵn bằng openpyxl: chỉ đổi ô, giữ nguyên workbook; khớp dòng theo khoá (mã, tên, đường dẫn), **không theo thứ tự dòng** — file xuất từ phần mềm khác hay bỏ dòng trống.
- Ô trống thường **không có** trong file xuất từ phần mềm khác: điền tạm một chữ ở phần mềm gốc rồi mới xuất, sửa xong nhập lại và **xuất lại mà kiểm**.
- File mẫu báo cáo: `File_Mau_Xuat_Bao_Cao_<Loai>_<VI|EN>.xlsx`; bản cũ `.bak-before-<việc>`. Hai ngôn ngữ = hai file mẫu.
- Định dạng số đặt trên ô Excel (cả cột), không trong dữ liệu; Page Setup (khổ giấy, header/footer công ty) đặt trong mẫu để mọi trang PDF xuất ra đều có.
- Đổi cấu hình add-in Office (web add-in) thì sửa part `xl/webextensions/webextension1.xml` trên bản sao — add-in không hiện trong `COMAddIns`.

## PowerPoint

- Deck chỉnh sửa được: plugin **ppt-master** (`/plugin install ppt-master@ppt-master`), hoặc skill Anthropic `pptx`. Muốn trang trình chiếu HTML thì skill `slides` trong `vendor/ui-ux-pro-max-skill`.
- Chưa có khuôn slide riêng được Sáng chốt → hỏi người xem và nơi trình chiếu; màu lấy theo bộ tài liệu cùng dự án (tài liệu kỹ thuật: navy `#1D3F73`, nhấn xanh lá `#2E9B45`; MP MES: `Theme.xaml`), không tự chế bảng màu mới.

## Script tiếng Việt trên Windows

| Bẫy | Cách tránh | Chi tiết |
|---|---|---|
| PowerShell 5.1 đọc `.ps1` UTF-8 không BOM theo ANSI | Ghi lại có BOM rồi parse-check, hoặc giữ `.ps1` ASCII và nạp chữ Việt từ file UTF-8 | [ps51-utf8-tieng-viet](references/ps51-utf8-tieng-viet.md) |
| `csc` và công cụ biên dịch khác đọc file không BOM theo codepage | Thêm BOM, `encoding='utf-8-sig'` | [bom-tieng-viet](references/bom-tieng-viet.md) |
| Python ghi lại file làm mất CRLF | `newline=''` cả lúc đọc lẫn ghi | [python-newline-crlf](references/python-newline-crlf.md) |
| `$vai` đè `$Vai`; hàm in chữ thành mảng trả về | Tên biến khác hẳn nhau, in bằng `Write-Host` | [powershell-bien-hoa-thuong](references/powershell-bien-hoa-thuong.md) |
| Heredoc Bash nuốt `\` | Mã có `\` viết bằng công cụ Write rồi chạy file | [bash-heredoc-gach-nguoc](references/bash-heredoc-gach-nguoc.md) |
| SendKeys bị bộ gõ telex đổi chữ | Dán clipboard thay vì gõ | [sendkeys-bo-go-tieng-viet](references/sendkeys-bo-go-tieng-viet.md) |
