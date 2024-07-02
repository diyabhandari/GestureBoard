$wshShell = New-Object -ComObject WScript.Shell
$audioLevel = 7  # Number of times to press the volume up key

1..$audioLevel | ForEach-Object { 
    $wshShell.SendKeys([char]175)
    Start-Sleep -Milliseconds 50
}