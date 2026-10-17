---
name: khbd-nhu-form-chuan
description: "Form chuẩn KHBD lớp 1D cô Như — mẫu là TUẦN 5_KHBD lớp 1D.docx (kể cả kiểu bảng); lề, bảng, giãn dòng, dòng tên bài"
---

> Nguồn: ghi nhớ `khbd-nhu-form-chuan`, cập nhật 2026-10-11. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

"Căn chỉnh lề như hôm bữa / form như hôm trước" = làm theo **`TUẦN 5_KHBD lớp 1D.docx`** (Sáng chỉ đích danh 11/10, "các bảng cũng phải giống"). Đừng lấy `KHBD TUẦN 5 - 1D.docx` làm mẫu bảng. Thư mục đã chuyển từ `3.Nhu` sang `C:\HCM_UTE\100.Nhu`.

- A4, lề trên 2 / dưới 2 / trái 3 / phải 2 cm (NĐ 30/2020); vùng chữ 16 cm.
- Times New Roman mọi run; cỡ 14 (bảng lịch 12).
- Giãn dòng **1,2** (line=288), after 0 — Sáng nói 1.15 rồi đổi "1.2 đi" (25/09).
- Đoạn ngoài bảng thụt đầu dòng 1 cm; gạch đầu dòng căn đều; dòng căn giữa/phải không thụt.
- Bảng lịch báo giảng: lưới [1365,774,714,1364,625,738,1860,1632].
- Bảng bài dạy chép y tblPr/tcPr của mẫu: 16 cm, hai cột 4536/4536 (không giữ tỉ lệ cũ), viền ngoài + dọc xám 7F7F7F, không TableGrid, không tcMar, không tô nền, không lặp tiêu đề. Hàng GV/HS: viết hoa đậm, kẻ dưới, giữa. Hàng gộp ô kẻ 4 cạnh, đậm: "TIẾT n" căn giữa (chỉ chữ TIẾT hoa, "(SGK trang …)" giữ thường), "n. MỤC" viết hoa; "a. …" giữ nguyên. Hàng nội dung kẻ trên. Mỗi bài MỘT bảng: Toán nhiều tiết tách bảng thì gộp lại, thay chữ "Tiết n" ngoài bảng bằng hàng TIẾT n.
- Tên mục: "III. CÁC HOẠT ĐỘNG DẠY HỌC".
- "Môn học: …<tab trái 6804>Lớp: 1D"; "Tên bài học:<tab giữa 4480>TÊN BÀI<tab trái 6804>Số tiết: n tiết". Tên bài dài thì "Số tiết" xuống dòng riêng, sát lề (thụt 1 cm).

11/10 tuần 6: `fix_khbd.py` (lề/đoạn) rồi `fix_tables.py in tpl out` (bảng) (scratchpad phiên ebf92ead, sẽ mất) — sửa XML bằng lxml trên bản sao, kiểm bằng Word xuất PDF + diff chữ, sao lưu "- ban goc.docx" cạnh file. Giữ chữ đỏ tích hợp; chữ xanh 1F4E79 đổi đen.

**Why:** các lần trước phải lục transcript mới ra thông số.
**How to apply:** KHBD tuần mới → áp nguyên danh sách này, đối chiếu với file tuần 5. Liên quan [ask-before-killing-user-apps](file-office-bi-khoa.md), [word-com-docx-gotchas](word-com-bay.md).
