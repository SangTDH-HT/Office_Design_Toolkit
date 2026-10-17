---
name: drawio-rhombus-anchor
description: "Trong draw.io, entryX/entryY là toạ độ hộp bao - với hình thoi chỉ 4 đỉnh mới có hình thật"
---

> Nguồn: ghi nhớ `drawio-rhombus-anchor`, cập nhật 2026-08-13. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

`exitX/exitY/entryX/entryY` trong draw.io là tỉ lệ trên **hộp bao (bounding box)**, không phải trên đường viền hình. Với `rhombus` (khối quyết định của lưu đồ), hộp bao chỉ chạm hình tại 4 đỉnh: `(0.5,0)` trên, `(1,0.5)` phải, `(0.5,1)` dưới, `(0,0.5)` trái. Mọi giá trị khác — `(0.75,0)`, `(1,0.25)`, `(0,0.75)` — rơi vào **góc trống ngoài hình thoi**, mũi tên đâm vào khoảng không. Người dùng phát hiện ngay khi nhìn ảnh xuất ra.

Vòng lặp "chờ" (nhánh Không quay lại chính nó) phải: thoát đỉnh trái/phải `(0/1, 0.5)` → ra lane bên → lên trên đỉnh khối → vào **đỉnh trên `(0.5, 0)`**. Hai mũi tên cùng vào đỉnh trên là chuẩn lưu đồ, không sao.

Hai điểm khác:
- Nhãn của cạnh đi vòng dài mặc định nằm giữa cạnh, tức lạc giữa hành lang. Ghim về gần nguồn bằng `x="-0.85"` trong `<mxGeometry relative="1" x="-0.85" as="geometry">` của **chính cạnh đó**.
- Lưu đồ một cột dễ cao 2500 px, thu vào khổ A4 thì chữ không đọc nổi. Ngắt sang cột 2 để tỉ lệ về khoảng 1,4 (ngang).

Kiểm chứng bằng CLI có sẵn trên máy: `& "C:\Program Files\draw.io\draw.io.exe" --no-sandbox -x -f png -p <trang> -s 2 -b 20 -o out.png file.drawio` rồi đọc ảnh — đừng tin XML hợp lệ là bố cục đúng.
