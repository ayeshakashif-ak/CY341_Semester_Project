rule rootkit_behavior_generic
{
    meta:
        description = "Detects potential rootkit behavior via suspicious API strings"
        author = "Ayesha"
        threat_type = "Rootkit"

    strings:
        $api1 = "NtQuerySystemInformation"
        $api2 = "ZwLoadDriver"
        $api3 = "HideDriver" ascii
        $str1 = "rootkit" nocase

    condition:
        any of ($api*) and $str1
}
