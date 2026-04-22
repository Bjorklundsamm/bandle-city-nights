#!/usr/bin/env bash
# Sends Shift+R to the running Ren'Py window to hot-reload scripts.
# Falls back to launching a new instance if Ren'Py isn't running.
RENPY="C:/Users/brofe/Documents/renpy-8.4.1-sdk/renpy.exe"
PROJECT="C:/Users/brofe/Documents/Projects/Bandle City Nights"

powershell.exe -NoProfile -Command "
if (Get-Process -Name 'renpy' -ErrorAction SilentlyContinue) {
    \$ws = New-Object -ComObject wscript.shell
    \$ws.AppActivate('Bandle City Nights')
    Start-Sleep -Milliseconds 200
    \$ws.SendKeys('+r')
} else {
    Start-Process '$RENPY' -ArgumentList '\"$PROJECT\"'
}
"
