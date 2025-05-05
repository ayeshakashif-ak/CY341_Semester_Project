rule keylogger_sample {
    strings:
        $c = "keylogger_string"
    condition:
        $c
}
