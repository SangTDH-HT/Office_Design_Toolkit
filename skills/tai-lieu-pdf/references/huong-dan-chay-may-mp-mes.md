---
name: mp-mes-bo-huong-dan-chay-may
description: "Bộ hướng dẫn chạy máy MP MES 2.0 (15/10/2026): 9 PDF ≤3 trang + tổng hợp + giám sát ở docs\\Huong-dan-van-hanh; ảnh thật chụp nền MES ngoài màn hình; ảnh đen = hiệu ứng động → tắt tạm ClientAreaAnimation"
---

> Nguồn: ghi nhớ `mp-mes-bo-huong-dan-chay-may`, cập nhật 2026-10-15. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Sáng 15/10/2026: "soạn file hướng dẫn thao tác chạy máy trên MP MES cho toàn bộ máy, có hình thực tế, 1 máy nhiều nhất 3 tờ A4, mỗi máy 1 file folder riêng, chữ to; 1 file tổng hợp chức năng các máy, 1 file chức năng giám sát xưởng".

Ra: `C:\MinhPhuc\MP_MES\docs\Huong-dan-van-hanh\` — 01-May-In-1 … 09-To-song (mỗi máy 3 trang), `Tong-hop-chuc-nang-cac-may.pdf` (3), `Chuc-nang-giam-sat-xuong.pdf` (4); nguồn HTML/ảnh `_nguon\`. Công cụ + cách làm lại: `tools\huong-dan-van-hanh\README.md` (chup-may.ps1, chup-khong-hieu-ung.ps1, tao_tai_lieu.py + noi_dung*.py). Chưa commit, chưa đưa Sáng duyệt bố cục.

Bẫy đã gặp:
- Cửa sổ WPF đặt ngoài màn hình + PrintWindow: màn có **hiệu ứng động** (lớp phủ CHỌN ĐƠN, chấm nhấp nháy tổ sóng, sọc Toàn xưởng) ra **ảnh đen**. Gốc đúng: tắt tạm SPI_SETCLIENTAREAANIMATION (MES tự tắt hiệu ứng theo nó), không lưu hồ sơ, trả lại ngay. Chế độ WPF vẽ phần mềm (registry DisableHWAcceleration) chữa được một màn nhưng làm đen màn khác — đừng dùng.
- Ô tích chọn đơn (Border) không ăn PostMessage chuột → đặt đơn bằng 2 câu UPDATE; tờ phiếu Bắt đầu sản xuất dựng in-process trên desktop ẩn (`ve-to-phieu.ps1`).
- TP "Lưu đơn" lưu thẳng không hỏi; "Chuyển ngày" bị chặn khi máy đang chạy; dừng dao tổ sóng không hỏi lý do (khai ở dòng ngừng khung Thời gian). TP: "chuẩn bị" vào sổ cộng chung ngừng KOKH.
- Dấu tiếng Việt dòng đầu trang tràn ngược lên trang trước khi h2 line-height thấp (Chrome in PDF) — soát bằng PyMuPDF span gần mép.

Liên quan *hub-mp-mes-minh-phuc*, [khong-chiem-chuot-khi-thu-ui](../../ui-ux-quy-trinh/references/thu-ui-khong-chiem-chuot.md), [chup-wpf-khong-dung-mp-shell-app](../../ui-ux-quy-trinh/references/chup-wpf-an-toan.md).
