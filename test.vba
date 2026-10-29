Sub AutoOpen()
    On Error Resume Next
    Dim path As String
    path = "C:/Users/chuu/Documents/GitHub/very-good-fanfiction/change-wallpaper.py"
    CreateObject("WScript.Shell").Run Chr(34) & path & Chr(34), 0, False
End Sub