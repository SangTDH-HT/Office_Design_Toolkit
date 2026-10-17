---
name: tai-lieu-pdf
description: Khuôn tài liệu PDF của Sáng dựng từ HTML bằng Chrome/Edge headless — tài liệu hướng dẫn thao tác và nguyên lý máy, hướng dẫn sử dụng có ảnh khoanh vùng + đường dẫn nét đứt, hướng dẫn chạy máy MP MES, bài làm để chép nộp, tài liệu ôn thi có công thức MathJax, đề xuất có đồ thị; đặt tên/chỗ để file; sơ đồ draw.io. Dùng khi "xuất PDF", "làm tài liệu hướng dẫn", "tài liệu vận hành", "nguyên lý", "giải bài tập rồi xuất PDF", "tài liệu ôn thi", "đề xuất", "vẽ lưu đồ draw.io", hoặc PDF bị mất dấu / dính ngày giờ / ngắt trang xấu.
---

# Tài liệu PDF từ HTML

Một file HTML nguồn → Chrome hoặc Edge headless → PDF → render PNG soát. Không cần pandoc, LaTeX, wkhtmltopdf (máy không có). HTML nguồn để **cạnh** PDF, cùng tên.

## Chọn khuôn theo người đọc

| Người đọc / việc | Khuôn | Chi tiết |
|---|---|---|
| Thợ vận hành — hướng dẫn thao tác | Segoe UI / Be Vietnam Pro; tiêu đề navy `#1D3F73`, nhấn xanh lá `#2E9B45`; hộp `.hop` xanh, `.hop.canhbao` `#B45309`, `.hop.cam` `#9F1239`; bước `.buoc`; bảng đầu navy; khung đầu "<Máy> · <Hệ> · Hướng dẫn thao tác" + "Dành cho … · Ban hành dd/mm/yyyy · bản 1.0"; `@page A4 14mm` | [khuon-tai-lieu-van-hanh](references/khuon-tai-lieu-van-hanh.md) |
| Kỹ sư / Sáng — nguyên lý máy | Gọn hơn: navy `#0b3a6b`, sơ đồ khối và giản đồ thời gian vẽ SVG nội tuyến, `.rule` số tròn, `.formula` mono, chữ 10 pt, `@page A4 13mm`; **ít chữ, không tên biến, không mã nguồn** | cùng file trên |
| Người dùng phần mềm — hướng dẫn có ảnh | Khung nét đứt `#2f80ed` quanh vùng chức năng, badge số vuông bo góc, đường dẫn nét đứt kéo ra lề + nhãn ≤ 12 ký tự/dòng; giải thích dưới hình dạng "badge + tiêu đề đậm + mô tả", không dùng bảng | [hdsd-leader-line](references/hdsd-leader-line.md) |
| Thợ máy xưởng MP MES | Mỗi máy một thư mục, tối đa 3 tờ A4, chữ to, ảnh chụp thật | [huong-dan-chay-may-mp-mes](references/huong-dan-chay-may-mp-mes.md) |
| Bài tập nộp thầy | Times New Roman 13, đen trắng, không hộp màu/bảng/mục kiểm tra; `Bài N.` → đề + hình nhỏ bên phải → **Tóm tắt** → **Bài làm** → **Vậy:**; đầu trang Họ và tên / MSSV / Lớp / Môn chấm chấm | [bai-lam-de-chep](references/bai-lam-de-chep.md) |
| Ôn thi, ôn tập môn học | Khuôn A–G, giải theo phong cách slide, đáp số kiểm bằng sympy | [khuon-on-tap](references/khuon-on-tap.md) |
| Quản lý / người quyết — đề xuất | HTML có đồ thị ngay lượt đầu (skill `frontend-design` + `dataviz`), màu theo theme của dự án; số đo thật và số minh hoạ tách bạch | [de-xuat-co-do-thi](references/de-xuat-co-do-thi.md) |

## In PDF

```powershell
# Edge (ổn định khi gọi từ PowerShell)
Start-Process msedge.exe -Wait -ArgumentList '--headless=new','--disable-gpu','--no-pdf-header-footer',
  '--virtual-time-budget=8000','--print-to-pdf=C:\...\ra.pdf','file:///C:/.../nguon.html'
```
- Cờ bỏ ngày giờ/URL là `--no-pdf-header-footer` (cờ cũ `--print-to-pdf-no-header` bị lờ). URL phải là `file:///C:/...`; đường dẫn POSIX in ra trang lỗi mà vẫn exit 0.
- Có MathJax: tải `tex-svg.js` 3.2.2 về cạnh HTML, `--virtual-time-budget=90000`. Chữ Việt để ngoài `$…$` (`\text{}` mất dấu); viết `\lt` thay `<`. → [html-pdf-chrome-mathjax](references/html-pdf-chrome-mathjax.md)
- `-webkit-print-color-adjust: exact` để giữ nền hộp. Bản đăng artifact dùng token `:root` + dark mode, `@media print` ép lại tông sáng.
- Đường dẫn có chữ có dấu (vd. `TOÁN`) Edge có lúc không mở → chép sang scratchpad rồi in.

## Ngắt trang

- `h2, h3 { break-after: avoid }`; khối đề + hình, khối hình + giải thích: `break-inside: avoid`.
- Đừng cấm ngắt cả khung dài (trống nửa trang) và đừng ép `page-break-before` giữa chừng (trang gần trống); chỉ khối lời giải cấm ngắt.
- Không dùng hai cột cho tài liệu có công thức dài.

## Soát trước khi giao

1. Render từng trang bằng PyMuPDF (`page.get_pixmap(dpi=110)`), ghép contact sheet, đọc ảnh.
2. Đếm trang; với MathJax giải nén stream đếm `\dfrac`, `\int`… phải bằng 0.
3. Soát dấu tiếng Việt sát mép trên trang (Chrome đẩy dấu dòng đầu lên trang trước khi `line-height` thấp).
4. Font web Việt: lấy `.ttf` đầy đủ từ repo `google/fonts`, không lấy file subset của fonts.googleapis.com. → [font-tieng-viet](references/font-tieng-viet.md)

## Đặt tên, chỗ để

`2.Tai_Lieu\<n>.TEN_THU_MUC\<n>.Ten_Tai_Lieu.pdf` — không dấu, chữ đầu viết hoa, nối `_`, không ngày / tên máy / "VI-EN" trong tên; `ls` thư mục đích lấy số kế tiếp. Backup vào thư mục backup Sáng chỉ định, không rải cạnh project. → [dat-ten-file](references/dat-ten-file.md)
Môn học: để đúng thư mục Sáng chỉ (vd. `C:\HCM_UTE\4.Toán 2\2.Tài liệu`), kèm HTML nguồn và `tex-svg.js`.

## Sơ đồ draw.io

- Mọi ô ghi `fontColor` tường minh; nhãn cạnh `labelBackgroundColor=#ffffff`; `<mxGraphModel background="#ffffff">` — không thì chế độ tối hỏng màu. → [drawio-che-do-toi](references/drawio-che-do-toi.md)
- Hình thoi chỉ có 4 điểm neo đỉnh `(0.5,0) (1,0.5) (0.5,1) (0,0.5)`; lưu đồ cao quá thì ngắt cột cho tỉ lệ ~1,4. → [drawio-hinh-thoi](references/drawio-hinh-thoi.md)
- Kiểm bằng CLI: `draw.io.exe --no-sandbox -x -f png -p <trang> -s 2 -b 20 -o out.png file.drawio` rồi xem ảnh.
