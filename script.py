import pyautogui

pyautogui.hotkey('alt', 'tab')

# message to be sent
message = "Ha"
# starting number
start = 1
# ending number
end = 100
# displays a counter before message
counter_on = True
# the script pauses on multiple of <pause_on> variable
pause_on = 100

for i in range(start, end + 1):
    if counter_on:
        pyautogui.write(str(i) + '. ' + message)
    else:
        pyautogui.write(message)

    pyautogui.press('enter')

    if(i % pause_on == 0):
        input('Press any key to continue...')
        pyautogui.hotkey('alt', 'tab')
