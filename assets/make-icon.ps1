# Erzeugt das RepackGuard-Icon als PNG (256). Robust, ohne Path-Kurven.
Add-Type -AssemblyName System.Drawing

$dir = Split-Path -Parent $PSCommandPath
$png  = Join-Path $dir "icon.png"
$ico  = Join-Path $dir "icon.ico"

function Draw-Icon([int]$size) {
    $bmp = New-Object System.Drawing.Bitmap($size, $size)
    $g   = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.Clear([System.Drawing.Color]::Transparent)
    $s = $size / 256.0

    # Hintergrund: abgerundetes Rechteck
    $c = 52 * $s
    $p = New-Object System.Drawing.Drawing2D.GraphicsPath
    $p.AddArc(0, 0, 2*$c, 2*$c, 180, 90)
    $p.AddArc($size-2*$c, 0, 2*$c, 2*$c, 270, 90)
    $p.AddArc($size-2*$c, $size-2*$c, 2*$c, 2*$c, 0, 90)
    $p.AddArc(0, $size-2*$c, 2*$c, 2*$c, 90, 90)
    $p.CloseFigure()
    $bgb = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
        (New-Object System.Drawing.Point(0,0)), (New-Object System.Drawing.Point($size,$size)),
        [System.Drawing.Color]::FromArgb(11,18,32), [System.Drawing.Color]::FromArgb(19,28,46))
    $g.FillPath($bgb, $p)
    $gb = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(31,43,64), (4*$s))
    $g.DrawPath($gb, $p)

    # Schild: Polygon (7 Punkte)
    $coords = @(@(128,46), @(196,72), @(196,128), @(128,216), @(60,172), @(60,128), @(60,72))
    $pts = New-Object 'System.Drawing.PointF[]' 7
    for ($i=0; $i -lt 7; $i++) {
        $pts[$i] = New-Object System.Drawing.PointF([single]($coords[$i][0]*$s), [single]($coords[$i][1]*$s))
    }
    $sb = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
        (New-Object System.Drawing.Point(0,0)), (New-Object System.Drawing.Point(0,$size)),
        [System.Drawing.Color]::FromArgb(56,189,248), [System.Drawing.Color]::FromArgb(37,99,235))
    $g.FillPolygon($sb, $pts)
    $sp = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(125,211,252), (5*$s))
    $g.DrawPolygon($sp, $pts)

    # Code-Klammern
    $cp = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(11,18,16), (12*$s))
    $cp.StartCap = [System.Drawing.Drawing2D.LineCap]::Round
    $cp.EndCap   = [System.Drawing.Drawing2D.LineCap]::Round
    $g.DrawLine($cp, [single](104*$s),[single](108*$s), [single](86*$s),[single](128*$s))
    $g.DrawLine($cp, [single](86*$s),[single](128*$s),  [single](104*$s),[single](148*$s))
    $g.DrawLine($cp, [single](152*$s),[single](108*$s), [single](170*$s),[single](128*$s))
    $g.DrawLine($cp, [single](170*$s),[single](128*$s), [single](152*$s),[single](148*$s))

    # Warnpunkt
    $darkBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(11,18,32))
    $warnBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(251,191,36))
    $g.FillEllipse($darkBrush, [single](117*$s),[single](161*$s),[single](22*$s),[single](22*$s))
    $g.FillEllipse($warnBrush, [single](123*$s),[single](167*$s),[single](10*$s),[single](10*$s))

    $g.Dispose()
    return $bmp
}

$b = Draw-Icon 256
$b.Save($png, [System.Drawing.Imaging.ImageFormat]::Png)
$b.Dispose()
Write-Output "PNG: $png"

$b2 = Draw-Icon 64
$b2.Save($ico, [System.Drawing.Imaging.ImageFormat]::Png)
$b2.Dispose()
Write-Output "ICO-Datei: $ico"

Get-ChildItem $png, $ico | Select-Object Name, Length
