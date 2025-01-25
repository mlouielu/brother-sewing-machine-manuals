# I Scraped Brother USA Website To Figure Out Which Sewing Machine Has One Function (Thread Cutter Button) That I Want

See the [full story here](https://blog.louie.lu/2025/01/24/i-scraped-brother-usa-website-to-figure-out-which-sewing-machine-has-one-function-thread-cutter-button-that-i-want/)

## Prerequisite

- requests
- lxml
- pdfgrep

## Run

```
# Download all the manuals
python brother_sewing_machines.py

# Get all the manual that said "thread cutter button"
pdfgrep -e '“Thread Cutter” button' -e "Thread cutter button" \
             manuals/*.pdf > matches

# Clean it up
awk -F: 'NR>2 {print $1}' matches | uniq | \
         sed 's|manuals/||' | sed 's|.pdf||'
```

## List of Brother sewing machine that has dedicate "thread cutter button"

* CS-8060
* CS-80
* CS-8150
* DZ820E
* EV1-LE
* EV1
* HE-120
* HE1
* HE-240
* Innov-is 1000
* Innov-is 1200
* Innov-is 1250D
* Innov-is 1500D-1500
* Innov-is 2500D
* Innov-is 2800D
* Innov-is 4000D-4000
* Innov-is 4500D
* Innov-is 4750D
* Innov-is 500D
* Innov-is 6000D
* Innov-is 6700D
* Innov-is 6750D
* Innov-is 900D
* Innov-is 950D
* Innov-is 990D
* Innov-is BP1400E
* Innov-is BP2100
* Innov-is BP2150L
* Innov-is BP3500D
* Innov-is BQ1350
* Innov-is BQ2450
* Innov-is BQ2500
* Innov-is BQ3050
* Innov-is BQ3100
* Innov-is BQ950
* Innov-is NQ1300PRW- Innov-is NQ1300
* Innov-is NQ1400E
* Innov-is NQ1600E
* Innov-is NQ1700E
* Innov-is NQ3500D
* Innov-is NQ3550W
* Innov-is NQ3600D
* Innov-is NQ3700D
* Innov-is NQ550PRW - Innov-is NQ550
* Innov-is NQ575PRW - Innov-is NQ575
* Innov-is NQ700PRW- Innov-is NQ700
* Innov-is NQ900PRW- Innov-is NQ900
* Innov-is NS1150E
* Innov-is NS1250E
* Innov-is NS1750D
* Innov-is NS1850D
* Innov-is NS2750D
* Innov-is NS2850D
* Innov-is PS500
* Innov-is PS700
* Innov-is VE2200
* Innov-is VE2300
* Innov-is VM5100
* Innov-is VM5200
* Innov-is VM6200D
* Innov-is VQ2400
* Innov-is VQ3000
* Innov-is XE1
* Innov-is XE2
* Innov-is XJ1
* Innov-is XJ2
* Innov-is XP1
* Innov-is XP2
* Innov-is XP3
* Innov-is XV8500D
* Innov-is XV8550D
* LB5000
* LB5500
* LB6770-6770PRW
* LB-6800
* LB7000
* NX-400Q-400
* NX-450-450Q
* NX570Q
* NX-600
* NX-650Q
* PC-420-420PRW
* PC-6500
* PE500
* PE525
* PE535
* PE540D
* PE545
* PE550D
* PE570
* PE-700-750D
* PE-700II-750D(USB)
* PE-770
* PE-780D
* PE800
* PE900
* PP1
* QC-1000
* SB3129
* SB3150
* SB4138
* SB7050E
* SB7500
* SB7900E
* SB8000
* SE1800
* SE1900
* SE1950
* SE2000
* SE-270D
* SE-350
* SE-400
* SE425
* SE600
* SE625
* SE630
* SE700
* SE725
