rule keylogger_memory_pattern
{
    meta:
        description = "Detects potential keylogger behavior in memory"
        author = "Ayela"
        category = "Keylogger"

    strings:
        $key1 = "GetAsyncKeyState"
        $key2 = "GetForegroundWindow"
        $key3 = "WriteFile"
        $str1 = "keylog" nocase

    condition:
        any of them
}
