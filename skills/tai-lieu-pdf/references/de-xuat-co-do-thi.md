---
name: de-xuat-phai-co-do-thi-dep
description: "Sáng 07/10/2026: bản đề xuất chỉ có chữ và bảng là chưa đạt — 'nên có đồ thị cho nó chuyên nghiệp, đồ thị phải đẹp'; giao đề xuất thì kèm bản HTML có đồ thị ngay lượt đầu"
---

> Nguồn: ghi nhớ `de-xuat-phai-co-do-thi-dep`, cập nhật 2026-10-14. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Sáng nhắn 07/10/2026, ngay sau khi em giao bản đề xuất đối chiếu dữ liệu MP MES dạng `.md` toàn chữ và bảng:
**"nên có đồ thị cho nó chuyên nghiệp, đồ thị phải đẹp nha"**.

**Why:** (em suy ra, anh không nói) đề xuất là thứ đưa Quản lý / Kỹ thuật / người quyết xem; chữ và bảng không cho thấy màn hình sẽ trông ra sao.

**How to apply:** (phạm vi là em suy ra: đề xuất / báo cáo cho người quyết — không phải ghi chú kỹ thuật hay file cho phiên code)
- Giao đề xuất thì kèm bản HTML có đồ thị ngay lượt đầu: số đo thật vẽ thành hình, mỗi chức năng chính một màn mẫu ghi rõ
  "số minh hoạ". File `.md` vẫn giữ làm bản gốc cho phiên code.
- Cách đã làm được việc: gọi skill `frontend-design` + `dataviz`; màu lấy từ `Theme.xaml` của MES rồi chạy `validate_palette.js`
  (bảng màu đã kiểm nằm ở mục 6b của `DOI-CHIEU-DU-LIEU.md`); một file Python sinh SVG nội tuyến
  (`C:\MinhPhuc\MP_MES\tools\dieu-phoi\dung_trang_doi_chieu.py` là mẫu: thanh, cầu thang, hai cột nối đường, hai chấm nối, lịch, thước đo);
  chụp thử bằng Chrome `--headless=new` qua cổng gỡ lỗi (Node 22 có sẵn WebSocket, không chiếm chuột) ở 1280 và 400 px, nền sáng và tối;
  lưu HTML cạnh file `.md` và publish Artifact riêng tư.
- Số đo thật và số minh hoạ không được lẫn: số đo để trần trên nền trang, màn mẫu nằm trong thẻ kiểu MES.
- Chụp nhanh không cần cổng gỡ lỗi (14/10): `chrome --headless=new --window-size=400,…` bị kẹp bề ngang ~500 px nên ảnh 400 px trông như tràn lề
  → bọc trang trong `<iframe style="width:400px">` rồi chụp cửa sổ 600 px. Headless theo nền tối của Windows: muốn xem nền sáng thì dựng bản `data-theme="light"`.
  Trang mới import CSS/đồ thị từ `dung_trang_thu_vien_s7.py` cho cùng bộ mặt (mẫu: `dung_trang_ngung_don_tp.py`).

Liên quan [thiet-ke-ui-dung-skill-frontend-design](../../ui-ux-quy-trinh/references/frontend-design-truoc.md), [mp-mes-giao-dien-theo-theme](../../ui-ux-quy-trinh/references/app-wpf-theo-theme.md), *mp-mes-doi-chieu-du-lieu*.
