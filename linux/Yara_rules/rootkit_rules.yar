rule rootkit_sample {
    strings:
        $b = "rootkit_string"
    condition:
        $b
}
