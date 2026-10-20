---
kind: forum-thread
id: "toolkitzone-forum/29039"
site: "toolkitzone.com"
board: "toolkitzone.com forum (tkzone skin)"
forum: null
skin: "tkzone"
thread_id: "29039"
title: "Just A Question"
original_url: "http://toolkitzone.com/forum/viewtopic.php?t=29039"
written: "2006-04-11T08:46:00"
last_post: "2006-04-11T20:29:00"
date_confidence: "exact"
captured: ["20070224065816", "20070224065836"]
author: "Ostridge"
repliers: ["Dominea", "Notsosuperhero"]
authors: ["Ostridge", "Dominea", "Notsosuperhero"]
posts_present: 4
pages_present: []
pages_total: null
posts_per_page: null
complete: null
encoding: latin-1
converter_version: "1"
gaps: []
source_captures:
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_312564", captured: "20070224065816", sha256: "871bfc87af301f1efdc5a66bdfc92fa4c6a0cbb1c9496879f39bc9893d0ca7d1", wayback_url: "https://web.archive.org/web/20070224065816/http://toolkitzone.com/forum/viewtopic.php?p=312564"}
  - {path: "wayback/toolkitzone.com/forum/viewtopic.php__p_312662", captured: "20070224065836", sha256: "ca81d36e363a801646c4ca39bdb4ff6c044cab85a51dd44645806262eba6d50d", wayback_url: "https://web.archive.org/web/20070224065836/http://toolkitzone.com/forum/viewtopic.php?p=312662"}
links: []
---

# Just A Question

### Ostridge · 2006-04-11 08:46 · #K312564

I Wrote This program and it compiles and everything but, you cant close the window unless you do ctrl + alt + delete. Can someone tell me whats wrong? Also could someone tell me how to make my window fullscreen no matter what the users resoultion is? Thanks!

**Code:**

```
//includes

#include <windows.h>

//message loop callback function

LRESULT CALLBACK fnMessageProcessor (HWND, UINT, WPARAM, LPARAM);

//function called automatically when the program starts

int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow)

{

        HWND hWnd;

        MSG msg;

        WNDCLASSEX wndclass;

        //set up window class

        wndclass.cbSize                 = sizeof(WNDCLASSEX);

        wndclass.style                  = CS_HREDRAW | CS_VREDRAW;

        wndclass.lpfnWndProc            = fnMessageProcessor;

        wndclass.cbClsExtra             = 0;

        wndclass.cbWndExtra             = 0;

        wndclass.hInstance              = hInstance;

        wndclass.hIcon                  = LoadIcon(NULL, IDI_APPLICATION);

        wndclass.hCursor                = LoadCursor(NULL, IDC_ARROW);

        wndclass.hbrBackground          = (HBRUSH)COLOR_MENU;

        wndclass.lpszMenuName           = NULL;

        wndclass.lpszClassName          = "Window Class";

//class name

wndclass.hIconSm                = LoadIcon(NULL, IDI_APPLICATION);

//register the window class

if(RegisterClassEx(&wndclass) == 0)

{

      //the program failed quit

   exit(1);

}

//create the window

hWnd = CreateWindowEx(

                  WS_EX_OVERLAPPEDWINDOW,

                  "Window Class",      //Class name

                  "Aldez",         //title bar text

                  WS_OVERLAPPEDWINDOW,

                  0,

                  0,

                  800,

                  600,

                  NULL,

                  NULL,

                  hInstance,

                  NULL);

//display the window

ShowWindow(hWnd, iCmdShow);

//process message until the program quits

while(GetMessage(&msg, NULL, 0, 0));

{

   TranslateMessage(&msg);

   DispatchMessage(&msg);

}

return (msg.wParam);

}

//message loop callback function

LRESULT CALLBACK fnMessageProcessor (HWND hWnd, UINT iMsg, WPARAM wParam, LPARAM lParam)

{

   switch(iMsg)

   {

      //call when window is first created

      case WM_CREATE:

         return(0);

      //call when the window is refreshed

      case WM_PAINT:

         return(0);

      //call when the user closes the window

      case WM_DESTROY:

         PostQuitMessage(0);

         return(0);

      default:

         return DefWindowProc(hWnd, iMsg, wParam, lParam);

   }

}
```

### Dominea · 2006-04-11 13:50 · #K312592

Concerning fullscreen: Your either gonna have to detect the resolution seeting on the running computer by quering register values or another route or you can check the MSDN and help files to see if there is a predefined setting/ flag you can set where the Windows API will detect it for you.
Also you dont need the return(0); where you have post quit message. Which is probably your problem. Your sending out the message for the window then your returning from the function. Windows handles this stuff for you.

### Notsosuperhero · 2006-04-11 19:04 · #K312654

break the cases in the switch statement. returning 0 from the message proc cases isn't it, I do that and my windows work completely fine.

### Ostridge · 2006-04-11 20:29 · #K312662

Thank you guys for the help, i got it working now. Smile
