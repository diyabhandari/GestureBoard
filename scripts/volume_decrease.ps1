$wshShell = New-Object -ComObject WScript.Shell
$audioLevel = 3  # Number of times to press the volume up key

1..$audioLevel | ForEach-Object {
    $wshShell.SendKeys([char]174)
    Start-Sleep -Milliseconds 100  # Adjust sleep time if needed
}