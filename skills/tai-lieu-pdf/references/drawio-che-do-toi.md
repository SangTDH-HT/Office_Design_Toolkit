---
name: drawio-dark-mode-mau-mac-dinh
description: "draw.io chế độ tối chỉ đụng vào màu KHÔNG khai báo - thiếu fontColor là chữ tàng hình, thiếu labelBackgroundColor là hộp đen sau nhãn"
---

> Nguồn: ghi nhớ `drawio-dark-mode-mau-mac-dinh`, cập nhật 2026-09-02. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Chế độ tối của draw.io **không lật ngược màu đã ghi rõ**. Nó chỉ thay giá trị mặc định của những thuộc tính bỏ trống. Nên bản vẽ hỏng ở đúng hai chỗ:

- Ô thiếu `fontColor=` → chữ lấy màu sáng của chủ đề tối, nằm trên nền pastel sáng thành mờ tịt.
- Nhãn thiếu `labelBackgroundColor=` → lấy nền tối mặc định, hiện ra **hộp đen** sau chữ.

Nhãn có ghi `labelBackgroundColor=#ffffff` vẫn trắng bình thường ở chế độ tối. Đừng đi gỡ nó — gỡ một thuộc tính chưa hề khai báo là vô tác dụng, phải **ghi đè giá trị tường minh**.

Cách vá một file cho hiển thị giống nhau ở mọi chủ đề:
- Mọi `<mxCell>` có style: thêm `fontColor` tường minh. Nền tối (luminance < 140) thì `#ffffff`, còn lại `#000000`.
- Nhãn của **cạnh** (`edge="1"`): `labelBackgroundColor=#ffffff` để hộp trắng cắt nét vẽ, không thì đường kẻ gạch ngang qua chữ.
- Chữ **trong khối** (vertex): bỏ hẳn nền nhãn, đặt trắng thì chữ bị hộp trắng bao giữa nền pastel.
- `<mxGraphModel background="#ffffff">` cho từng trang.

Nền lưới đen quanh bản vẽ là giao diện app, không nằm trong file. Tắt bằng `%APPDATA%\draw.io\config.json`: thêm `"darkMode": false, "ui": "kennedy"` rồi thoát hẳn app mở lại.

Kiểm chứng bằng CLI như [drawio-rhombus-anchor](drawio-hinh-thoi.md). Xuất PNG ở `-s 1` thì chữ đen bị viền xanh/cam do khử răng cưa subpixel của Chromium — lấy mẫu điểm ảnh thấy màu trội là `(0,0,0)` là đúng, đừng tưởng sai màu.
