---
name: mp-mes-giao-dien-theo-theme
description: "Mọi màn/hộp thoại MP MES phải lấy màu, phông, style từ Theme chung - tự chế phong cách riêng là bị chê xấu"
---

> Nguồn: ghi nhớ `mp-mes-giao-dien-theo-theme`, cập nhật 2026-09-06. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

Sáng chê "máy tính đang bị xấu á" khi cửa sổ Máy tính được dựng theo phong cách
macOS: khung bạc gradient, ba nút tròn đỏ-vàng-xám, cột phép tính cam, phông
Segoe UI, `WindowStyle=None + AllowsTransparency`.

**Why:** MP MES có bộ mặt thống nhất — nền be `Choi.NenChinh`, thẻ trắng bo góc
`BoGoc.The`, phông `Phong.Chinh` (Be Vietnam Pro), màu nhấn `Choi.Nhan` đổi theo
máy đang chọn. Một cửa sổ tự chế bảng màu riêng đặt cạnh phần còn lại thì lạc hẳn
ra, nhìn như của chương trình khác dán vào. Hộp thoại nhà (xem `HopThoaiNhap.cs`)
đều dùng khung cửa sổ Windows bình thường chứ không vẽ thanh tiêu đề riêng.

**How to apply:** trước khi dựng màn mới, đọc `Theme/Theme.xaml` (token `Mau.*`,
`Choi.*`, `CoChu.*`, `BoGoc.*`, `Phong.*`) và `Theme/Controls.xaml` (`Nut.Nen`,
`Nut.Chinh`, `Nut.Phu`, `Nut.PhimSo`, `Nut.Ribbon`) rồi dùng lại, đừng ghi mã màu
thẳng vào file. Bàn phím số thì `Nut.PhimSo` đã có sẵn cỡ 58 px, viền, bóng và lề
`0,0,12,12` — bù lề âm `0,0,-12,-12` ở Grid chứa nó.

Cây XAML dựng bằng `XamlReader.Parse` không thấy từ điển tài nguyên của ứng dụng
lúc phân tích, nên phải dùng `DynamicResource` cho mọi tham chiếu; `StaticResource`
ném "Cannot find resource" ngay, còn `Style.BasedOn` thì không nhận DynamicResource
— gán thẳng `Style='{DynamicResource ...}'` cho từng control rồi đè màu bằng thuộc
tính cục bộ. Liên quan: *mp-mes-vong-nghiem-thu*.
