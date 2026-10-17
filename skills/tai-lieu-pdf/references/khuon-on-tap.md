---
name: khuon-on-tap
description: "Khuôn tài liệu ôn thi / ôn tập môn học Sáng đã nhận (Toán 1, Toán 2, Vật lý 1, Tin học đại cương) — tổng hợp từ các lần giao 09–10/2026"
---

> Tổng hợp từ các ghi nhớ `toan1-hcmute-giua-ky-bai-1-10`, `toan2-hcmute-chuong-6-9`, `tin-hoc-dai-cuong-nong-lam-on-thi`,
> `vatly1-hcmute-pham-vi-mon` (09–10/2026). Phần riêng của từng môn (đề, chỗ slide in sai) không chép vào đây.

## Bố cục

| Phần | Nội dung |
|---|---|
| A | Kiến thức trọng tâm theo phạm vi thi (hỏi phạm vi trước: giữa kỳ hay cuối kỳ, chương nào) |
| B | Các dạng bài: cách nhận dạng, cách giải, cách trình bày |
| C | Giải **mọi** ví dụ + bài tập có trong slide, theo thứ tự slide |
| D | Bài tự luận kiểu đề thi (lấy từ đề thật Sáng chụp nếu có) |
| E/F | Lời giải chi tiết, sang trang mới |
| G | Mẹo, lỗi hay gặp, tờ A4 công thức (hai mặt, để chép tay) |

Bản nhỏ hơn đã giao: "Công thức và cách giải theo dạng" (4 trang), "Bài tập luyện theo dạng" (11 dạng × 3 bài, ô kẻ dòng để giải, lời giải ở phần 2).

## Cách viết lời giải

- **Giải theo phong cách slide của giảng viên**: "Giải.", "Đặt … thì …", "Khi đó", "Vậy … (đvdt)".
- Đáp số kiểm bằng sympy trước khi ghi; công thức Excel cho Excel thật tính qua COM.
- Đáp án sưu tầm trên mạng thường sai (đã gặp 18–33 đáp án sai mỗi bộ) — kiểm lại từng câu, câu hỏng đề thì bỏ.
- Slide in sai hoặc mơ hồ: giữ nguyên đề, ghi chú chỗ sai và đáp số đúng trong tài liệu.
- Đọc slide Toán bằng **ảnh** (render trang lưới 2×2, 88 dpi): `page.get_text()` ra rác ở mọi công thức.

## Trình bày

- Bìa "Biên soạn: Nguyễn Hữu Sáng" khi Sáng bảo ghi người biên soạn.
- HTML → Edge headless → PDF, MathJax SVG (xem [html-pdf-chrome-mathjax](html-pdf-chrome-mathjax.md)).
- `.dang` cho phép ngắt trang, chỉ `.giai` cấm ngắt; head.html chung có script dò công thức tràn khung (ghi `data-overflow`, đọc bằng `msedge --dump-dom`).
- Bài làm để chép nộp là khuôn khác — xem [bai-lam-de-chep](bai-lam-de-chep.md).
