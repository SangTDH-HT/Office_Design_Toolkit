---
name: mp-mes-man-tram-1280x1024
description: "Máy trạm MP MES màn 1280×1024: vùng trang THẬT 1204×817, có dải cảnh báo 1204×764 (số 1204×860 cũ là sai); Trang chủ cả ba loại máy co giãn từ 11/10 qua lớp chung CoGianTheoMan; soát bằng ve-trang-chu.ps1 -Loai in|tp|song"
---

> Nguồn: ghi nhớ `mp-mes-man-tram-1280x1024`, cập nhật 2026-10-11. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Màn máy trạm (tổ sóng, Sáng xác nhận 23/09/2026) là **1280×1024**. Số cũ "vùng nội dung
~1204×860" là SAI và là gốc lỗi "bị che" Sáng chụp 11/10/2026. Đo đúng khung MainWindow
(cửa sổ phóng to trừ thanh tác vụ 48 + tiêu đề 31; trang trừ thanh trái 76, thanh đầu 70,
dải nút 58):
- **1204×817**, khi có dải cảnh báo (~53 px) chỉ còn **1204×764**;
- 1920×1080 cho 1844×873 (820 khi có dải cảnh báo).

**Trang chủ co giãn theo màn (11/10/2026)** — tổ sóng chiều (gói 1.10 lần 2), máy in + thành phẩm tối (Sáng: "làm tiếp phần kích cỡ phần mềm cho các máy khác", gói lần 4 19:01):
- Lớp chung `Views\CoGianTheoMan.cs`: cả lưới `goc` co đều một hệ số (LayoutTransform), hệ số = cao vùng trang / cao TỰ NHIÊN (màn tự đo bằng Measure bề cao vô hạn), kẹp [0,75; 1,35], bề rộng logic không hẹp hơn bố cục đã dựng. Co ngay, phóng chỉ khi dư 2%; soát lại mỗi 2 giây; chạm sàn thì `cuonGoc` cho cuộn. Một lượt soát 0,3–0,5 ms (tối đa ~8 ms).
- Mỗi màn bọc `goc` trong ScrollViewer `cuonGoc`; Quản lý ở trạm khoá `goc` chứ không khoá Content (khoá Content là chặn luôn cuộn).
- Tổ sóng giữ hàm đo riêng (hai hàng sao chia theo tỉ lệ cao cần, danh sách đơn kế tiếp tính 96 px). Chuyển sang lớp chung ra ĐÚNG hệ số cũ ở cả sáu cỡ màn.
- Máy in: cao tự nhiên tính ĐỦ sáu trạm mực (mỗi dòng là ô nhập, trang không bắt thợ cuộn). Đơn 76 + hàng giữa 416 + hàng lỗi · trạm mực 408 (ô lỗi chỉ 301).
- Hệ số đạt:

  | Màn | tổ sóng | máy in | thành phẩm |
  |---|---|---|---|
  | 1280×1024 | 0,978 | 0,87 | 0,941 |
  | 1280×1024 có dải cảnh báo | 0,911 | 0,811 | 0,876 |
  | 1920×1080 | 1,047 | 0,932 | 1 |
- Trước khi sửa, ở 1280×1024: máy in ô lỗi đè nhau mất nhãn, sáu trạm mực chỉ thấy 3–4; thành phẩm ô lỗi đè nhau (dấu tiếng Việt của tên lỗi bị cắt nên đọc ra "SONG", "KHAC") và mất số BS/ECT/BCT/trọng lượng.
- **Chờ Sáng xem trên màn thật:** máy in 0,87 (0,81 lúc có dải) làm chữ chú thích nhỏ còn ~9–10 px. Nếu anh chê nhỏ thì có hai hướng: cho trạm 5–6 cuộn (hệ số ~0,98), hoặc làm dòng trạm mực thấp hơn.

**How to apply:**
- Soát màn: `tools\kiem-thu-giao-dien\ve-trang-chu.ps1 -Loai in|tp|song -Ra <thư mục> [-Bin <out>]`. Nó dựng màn NGOÀI cửa sổ, nên không có PresentationSource và Loaded không nổ (Trang chủ máy in / TP gắn PLC + SQL trong Loaded). Rồi vẽ 6 cỡ màn có/không dải cảnh báo ra PNG; báo hệ số, cần/có từng hàng, chỗ bị cắt / tràn / chữ cụt, khung cuộn đang giấu dòng, và ms một lượt soát.
- `ve-trang-chu-song.ps1` (bản cửa sổ, chỉ tổ sóng) vẫn chạy được.
- Bị cắt phải dò bằng `LayoutInformation.GetLayoutClip`, không so DesiredSize với RenderSize: WPF xếp phần tử ĐỦ cỡ rồi mới cắt bằng layout clip.
- Đừng dựng `MP.Shell.App` trong công cụ chụp, xem [chup-wpf-khong-dung-mp-shell-app](chup-wpf-an-toan.md).
- Bài MES thật `tools\kiem-thu-thua-thieu\thu-thua-thieu.ps1 -Bin <out> -Khoi in,dan` đạt 19 mục trên bản này. Khối song bị chặn khi bản sao SQL đã có kế hoạch tổ sóng trong ngày (nó tự dừng trước khi đụng gì).

Liên quan [mp-mes-giao-dien-theo-theme](app-wpf-theo-theme.md), *gop-to-song-vao-mp-mes*, *mp-mes-dong-goi-ban-phat-hanh*.
