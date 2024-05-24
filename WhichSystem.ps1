function Get-TTL {
    param (
        [string]$ipAddress
    )

    $pingResult = Test-Connection -ComputerName $ipAddress -Count 1 -ErrorAction SilentlyContinue
    if ($pingResult) {
        $ttl = $pingResult.ResponseTimeToLive
        if ($ttl -ge 127) {
            return "Windows"
        }
        elseif ($ttl -eq 64) {
            return "Linux"
        }
    }
    return "Desconocido"
}

$ipAddress = Read-Host "Introduce la dirección IP: "
$osType = Get-TTL -ipAddress $ipAddress
Write-Host "El TTL para $ipAddress es $($osType.TTL)."
Write-Host "El sistema operativo probable es: $osType"
