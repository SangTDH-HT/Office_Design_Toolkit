---
name: chup-wpf-khong-dung-mp-shell-app
description: "Công cụ chụp màn MES: dựng MP.Shell.App rồi bơm dispatcher là OnStartup chạy, MES thật khởi động (nối PLC) trên desktop ẩn — dựng Application trống; $rd.Source trong PowerShell thành thêm khoá"
---

> Nguồn: ghi nhớ `chup-wpf-khong-dung-mp-shell-app`, cập nhật 2026-10-11. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Ngày 11/10/2026 16:59, `ve-trang-chu-song.ps1` bản đầu làm `$mes.CreateInstance('MP.Shell.App')` + `InitializeComponent()` rồi đợi bằng `Dispatcher.PushFrame`. Hậu quả: MES khởi động thật trên desktop ẩn khoảng 4 phút, đúng trạm MI1 nối PLC thật .245, tới khi bị giết.

Lý do: constructor của `System.Windows.Application` hẹn OnStartup lên dispatcher, nên lần bơm dispatcher ĐẦU TIÊN là chạy OnStartup. Không cần gọi `Run()`.

Lần đó may không gửi lệnh PLC nào: log không có dòng lệnh, DB1/DB2 sạch, config.json được trả lại.

`tools\kiem-thu-quan-ly\ve-tab-du-lieu.ps1` (10/10) dính cùng bẫy, đã sửa 11/10.

Cách đúng, dùng ở cả hai công cụ:
- `New-Object System.Windows.Application`.
- Nạp `Theme/Theme.xaml`, `Theme/Icons.xaml`, `Theme/Controls.xaml` theo đúng thứ tự, qua `pack://application:,,,/MP.MES;component/...`.
- Rồi gọi `ThemeManager.GhiNhoGoc()` + `ApDung(AppConfig.Data.Theme)`.

**Bẫy PowerShell:** ResourceDictionary là IDictionary, nên `$rd.Source = [Uri]...` THÊM một khoá tên "Source" chứ không đặt thuộc tính. Kết quả là từ điển rỗng và lỗi "Cannot find resource named 'The'". Phải đặt bằng reflection: `[System.Windows.ResourceDictionary].GetProperty('Source').SetValue($rd, $uri)`.

**Why:** chụp màn mà bật nhầm MES thật là có thể gửi lệnh tới PLC thật đang sản xuất.

**How to apply:**
- Mọi script dựng view MES ngoài phần mềm: không bao giờ tạo `MP.Shell.App`.
- Grep `CreateInstance('MP.Shell.App')` trước khi chạy một công cụ chụp cũ.

Liên quan [mp-mes-man-tram-1280x1024](co-gian-theo-man.md), [khong-chiem-chuot-khi-thu-ui](thu-ui-khong-chiem-chuot.md).
