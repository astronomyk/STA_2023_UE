J/A+A/397/147       Activity-rotation relationship in stars (Pizzolato+ 2003)
================================================================================
The stellar activity-rotation relationship revisited: Dependence of saturated
and non-saturated X-ray emission regimes on  stellar mass for late-type dwarfs.
    Pizzolato N., Maggio A., Micela G., Sciortino S., Ventura P.
   <Astron. Astrophys. 397, 147 (2003)>
   =2003A&A...397..147P
================================================================================
ADC_Keywords: Stars, late-type ; X-ray sources ; Photometry, UBV
Keywords: stars: activity - stars: late-type - X-rays: stars

Abstract:
    We present the results of a new study on the relationship between
    coronal X-ray emission and stellar rotation in late-type main-sequence
    stars. We have selected a sample of 259 dwarfs in the B-V range
    0.5-2.0, including 110 field stars and 149 members of the Pleiades,
    Hyades, {alpha} Persei, IC 2602 and IC 2391 open clusters. All the
    stars have been observed with ROSAT, and most of them have
    photometrically-measured rotation periods available. Our results
    confirm that two emission regimes exist, one in which the rotation
    period is a good predictor of the total X-ray luminosity, and the
    other in which a constant saturated X-ray to bolometric luminosity
    ratio is attained; we present a quantitative estimate of the critical
    rotation periods below which stars of different masses (or spectral
    types) enter the saturated regime.

File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe         80        .   This file
stars.dat      61      258   Star positions (from Simbad)
table1.dat     61      110   Field dwarf sample
table2.dat     68      149   Cluster stars: Pleiades, IC 2602, IC 2391,
                              {alpha} Persei and Hyades
refs.dat       85       28   References
--------------------------------------------------------------------------------

See also:
    J/A+A/341/751 : ROSAT HRI observations of the Pleiades (Micela+ 1999)

Byte-by-byte Description of file: stars.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1- 10  A10   ---     Name      Star name
  18- 19  I2    h       RAh       Right ascension (J2000.0)
  21- 22  I2    min     RAm       Right ascension (J2000.0)
  24- 27  F4.1  s       RAs       Right ascension (J2000.0)
      29  A1    ---     DE-       Declination sign (J2000.0)
  30- 31  I2    deg     DEd       Declination (J2000.0)
  33- 34  I2    arcmin  DEm       Declination (J2000.0)
  36- 37  I2    arcsec  DEs       Declination (J2000.0)
  41- 61  A21   ---     SName     Simbad designation
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table1.dat
--------------------------------------------------------------------------------
   Bytes Format Units     Label      Explanations
--------------------------------------------------------------------------------
   1- 10  A10   ---       Name       Name
  12- 16  F5.2  pc        Dist       ? Distance
  18- 21  F4.2  mag       B-V        B-V colour index
  23- 28  F6.2  mag       Vmag       V magnitude
      31  A1    ---     l_Per        Limit flag on Per
  32- 36  F5.2  d         Per        Period
  38- 39  A2    ---     r_Per        Reference for the period, in refs.dat file
  42- 46  F5.2  [10-7W]   logLX      X-ray luminosity
  48- 49  A2    ---     r_logLX      Reference for X-ray luminosity,
                                      in refs.dat file
  52- 56  F5.2  [---]     logLX/Lbol Bolometric-to-X-ray luminosity ratio
  58- 61  F4.2  solMass   Mass       Mass
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table2.dat
--------------------------------------------------------------------------------
   Bytes Format Units     Label       Explanations
--------------------------------------------------------------------------------
   1- 12  A12   ---       Cluster     Cluster name
  14- 23  A10   ---       Name        Name
  25- 27  I3    pc        Dist        ? Distance
  29- 32  F4.2  mag       B-V         B-V colour index
  35- 39  F5.2  mag       Vmag        V magnitude
  41- 45  F5.2  d         Per         Period
  47- 48  I2    ---     r_Per         Reference for the period, in refs.dat file
  50- 54  F5.2  [10-7W]   logLX       X-ray luminosity
  56- 57  I2    ---     r_logLX       Reference for X-ray luminosity,
                                       in refs.dat file
  59- 63  F5.2  [---]     logLX/Lbol  Bolometric-to-X-ray luminosity ratio
  65- 68  F4.2  solMass   Mass        Mass
--------------------------------------------------------------------------------

Byte-by-byte Description of file: refs.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  2  A2    ---     Ref       Reference code
   4- 22  A19   ---     BibCode   BibCode
  24- 43  A20   ---     Aut       author's name
  47- 86  A40   ---     Com       Comments
--------------------------------------------------------------------------------

History:
    From electronic version of the journal
================================================================================
(End)                                       Patricia Bauer  [CDS]    25-Mar-2003
