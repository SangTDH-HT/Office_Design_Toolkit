---
name: khuon-tai-lieu-van-hanh
description: "Khuôn HTML → PDF cho tài liệu hướng dẫn thao tác và tài liệu nguyên lý máy mà Sáng đã duyệt (09/2026–10/2026)"
---

> Tổng hợp từ các bộ tài liệu vận hành và nguyên lý Sáng đã nhận; đã lược tên dự án.

## Hai loại, hai bộ mặt

| | Hướng dẫn thao tác | Nguyên lý máy |
|---|---|---|
| Người đọc | Thợ vận hành | Kỹ sư, Sáng |
| Font | Segoe UI / Be Vietnam Pro | như bên trái, chữ 10 pt |
| Màu | tiêu đề navy `#1D3F73`, nhấn xanh lá `#2E9B45` | navy `#0b3a6b` |
| Khối | hộp `.hop` (xanh), `.hop.canhbao` (`#B45309`), `.hop.cam` (`#9F1239`); bước đánh số `.buoc`; bảng `.bang` đầu navy | `.fig` + SVG vẽ tay (sơ đồ khối, giản đồ thời gian thanh ngang), `.rule` số tròn, `.formula` khối mono, `.box` / `.box.warn` |
| Đầu trang | khung `.dau`: "<Máy> · <Hệ> · Hướng dẫn thao tác" + meta "Dành cho … · Ban hành dd/mm/yyyy · bản 1.0" | tiêu đề + một dòng mục đích |
| Trang in | `@page A4 14mm` | `@page A4 13mm` |
| Chú thích ảnh | số xanh dương `#2f80ed` | — |

## Luật nội dung

- **Ít chữ.** Không tên biến/tag, không chân khối, không mã nguồn trong tài liệu cho thợ hay cho Sáng. Sơ đồ trình tự (van, động cơ, bước)
  thay cho đoạn văn — bản "rối, nhiều chữ quá" từng bị trả lại.
- Sơ đồ vẽ thẳng bằng SVG nội tuyến trong HTML — in headless ra đúng, không cần ảnh.
- Ảnh chụp màn hình dán vào chat **không nằm trên đĩa**: hoặc vẽ lại khung giao diện bằng HTML/CSS (`.pop`, `.steps`, `.ring` dùng lại
  được), hoặc xin Sáng bỏ PNG vào thư mục.
- Màn có menu thiết bị (đầu cân, biến tần…) vẽ thành chip kiểu màn LCD (`.lcd`).
- Bản đăng artifact chuyển màu sang token `:root` có dark mode; `@media print` ép lại tông sáng.

## In và soát

`msedge.exe --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=<out> --virtual-time-budget=8000 file:///<html>` —
ra đúng bố cục, có webfont. Xem lại bằng PyMuPDF render trang → ghép contact sheet.
Đừng ép `page-break-before` lên `h2` giữa chừng: dễ để lại trang gần trống. Đặt tên theo [dat-ten-file](dat-ten-file.md).
