---
name: hdsd-anh-khoanh-vung-leader-line
description: "Kiểu chú thích ảnh Sáng muốn cho tài liệu hướng dẫn, và script sinh PDF tái dùng được"
---

> Nguồn: ghi nhớ `hdsd-anh-khoanh-vung-leader-line`. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

Tài liệu hướng dẫn có ảnh phải chú thích kiểu: khung nét đứt xanh #2f80ed quanh vùng chức năng, badge số vuông bo góc, **đường dẫn nét đứt kéo ra lề** kèm nhãn ngắn; phần giải thích nằm dưới hình dạng "badge + tiêu đề đậm + đoạn mô tả", không phải bảng.

**Why:** Sáng đưa mẫu trang hướng dẫn của máy đời trước và nói "ví dụ như thế này nè" sau khi bản đầu dùng badge dán thẳng lên ảnh + bảng giải thích.

**How to apply:** dùng lại `nguon_tao_tai_lieu*.py` trong `D:\Du_An_Tot_Nghiep_Thang_May\FILE_DO_AN_TOT_NGHIEP\7.HUONG_DAN_SU_DUNG\` — hàm `annotate()` dựng cả ảnh lẫn chú thích trong một SVG có viewBox rộng hơn ảnh để chừa lề nhãn; `side` l/r/t/b + `at` là toạ độ nhãn trong hệ pixel ảnh. Hai bẫy đã vấp: nhãn 2 dòng ở cạnh trên/dưới bị viewBox cắt (nới `miny`/`h`), và hai nhãn cùng cạnh cách nhau dưới ~90 px là chồng chữ. Xuất PDF bằng Chrome headless với `--no-pdf-header-footer` (cờ `--print-to-pdf-no-header` không còn ăn), rồi đóng số trang bằng PyMuPDF. Ngắt trang: bỏ page-break cứng, cho `.h2 { page-break-before: always }` và gắn class `nb` cho mục nào muốn chảy tiếp — xem [pdf-tu-html-bang-chrome-mathjax](html-pdf-chrome-mathjax.md).

**Cập nhật 13/09/2026 — bộ dựng cho MP MES:** `C:\MinhPhuc\MP_MES\tools\hdsd-lay-don-gop-don\`
(`hdsd_lib.py` ghép ảnh + vẽ leader line SVG, `hinh_hdsd.py` toạ độ cắt/nhãn,
`tao_hdsd.py` dựng HTML → Chrome PDF, `chup-hdsd.ps1` lái app chụp cả lượt gộp).
Bài học: nhãn ở lề phải NGẮN (≤ ~12 ký tự/dòng) — lề tự tính theo nhãn dài nhất,
nhãn dài là ảnh co còn 40 mm không đọc được; giải thích dài để dưới hình dạng
"badge + tiêu đề đậm + mô tả". Hai hình cạnh nhau thì bọc mỗi hình trong
`.khoi` (figure + giải thích) và `page-break-inside: avoid`, không thì phần giải
thích thành cột thứ ba của flex. Bản gốc nguon_tao_tai_lieu*.py trên D: không còn
tìm thấy (13/09/2026).
