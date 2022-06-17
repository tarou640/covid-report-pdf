for /r %%f in (*.csf) do (call:convert_Fromsjis_Toutf8 %%f)
exit

REM -M=以下のURLはサクラエディタのマクロの配置場所に合わせて記述してください。
:convert_Fromsjis_Toutf8
"C:\Program Files\sakura\sakura.exe"  %1 -M=C:\Users\kifuzin_10\Documents\GitHub\covid-report-pdf\temp\convert_Fromsjis_Toutf8.mac
