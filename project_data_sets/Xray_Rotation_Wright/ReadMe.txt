J/ApJ/743/48 Stars with rotation periods and X-ray luminosities (Wright+, 2011)
================================================================================
The stellar-activity-rotation relationship and the evolution of stellar dynamos.
    Wright N.J., Drake J.J., Mamajek E.E., Henry G.W.
   <Astrophys. J., 743, 48 (2011)>
   =2011ApJ...743...48W
================================================================================
ADC_Keywords: Clusters, open ; Stars, late-type ; Stars, normal ; X-ray sources
              Magnetic fields
Keywords: stars: activity - stars: coronae - stars: evolution -
          stars: late-type - stars: magnetic field - stars: rotation -
          X-rays: stars

Abstract:
    We present a sample of 824 solar and late-type stars with X-ray
    luminosities and rotation periods. This is used to study the
    relationship between rotation and stellar activity and derive a new
    estimate of the convective turnover time. From an unbiased subset of
    this sample the power law slope of the unsaturated regime,
    L_X_/L_{bol}_{propto}Ro^{beta}^, is fit as {beta}=-2.70+/-0.13. This
    is inconsistent with the canonical {beta}=-2 slope to a confidence of
    5{sigma}, and argues for an additional term in the dynamo number
    equation. From a simple scaling analysis this implies
    {Delta}{Omega}/{Omega}{propto}{Omega}^0.7^, i.e. the differential
    rotation of solar-type stars gradually declines as they spin down.
    Super-saturation is observed for the fastest rotators in our sample
    and its parametric dependencies are explored. Significant correlations
    are found with both the corotation radius and the excess polar
    updraft, the latter theory providing a stronger dependence and being
    supported by other observations. We estimate mass-dependent empirical
    thresholds for saturation and super- saturation and map out three
    regimes of coronal emission. Late F-type stars are shown never to pass
    through the saturated regime, passing straight from super-saturated to
    unsaturated X-ray emission. The theoretical threshold for coronal
    stripping is shown to be significantly different from the empirical
    saturation threshold (Ro<0.13), suggesting it is not responsible.
    Instead we suggest that a different dynamo configuration is at work in
    stars with saturated coronal emission. This is supported by a
    correlation between the empirical saturation threshold and the time
    when stars transition between convective and interface sequences in
    rotational spin-down models.

Description:
    Photometric and derived stellar parameters for 824 solar- and
    late-type stars from nearby open clusters and the field, including
    rotation periods and X-ray luminosities.

File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe         80        .   This file
catalog.dat   185      824   Activity-rotation properties for 824 stars --
                              updated version by the author
refs.dat      131       65   References
--------------------------------------------------------------------------------

Byte-by-byte Description of file: catalog.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   1- 23  A23   ---     Name     Default source name (1)
  25- 30  I6    ---     HD       ? Henry Draper catalog number (Cat. III/135)
  32- 37  I6    ---     HIP      ? Hipparcos catalog number (Cat. I/239)
  39- 45  A7    ---     GJ       Catalog of nearby stars source name (Cat. V/70)
  47- 55  A9    ---     GCVS     ? General Catalog of Variable Stars source name
                                   (Cat. B/gcvs)
  57- 72  A16   ---     2MASS    2MASS source name (HHMMSSss+DDMMSSs; J2000 -
                                   Cat. II/246)
  74- 75  I2    h       RAh      ? Right Ascension J2000 (hours)
  77- 78  I2    min     RAm      ? Right Ascension J2000 (minutes)
  80- 84  F5.2  s       RAs      ? Right Ascension J2000 (seconds)
      86  A1    ---     DE-      ? Declination J2000 (sign)
  87- 88  I2    deg     DEd      ? Declination J2000 (degrees)
  90- 91  I2    arcmin  DEm      ? Declination J2000 (minutes)
  93- 96  F4.1  arcsec  DEs      ? Declination J2000 (seconds)
  98-105  A8    ---     Cluster  ? Name of open cluster that star is part of
                                   (or 'Field')
 107-111  F5.1  pc      Dist     ? Distance to star (2)
 113-117  F5.2  mag     Vmag     ? Observed V magnitude of star
 119-122  F4.2  mag     V-K      Dereddened V-K colour of star (3)
 124-128  A5    ---     SpT      ? Spectral type of star
 130-132  A3    ---   r_SpT      ? Reference for spectral type, in refs.dat file
 134-138  F5.2  [10-7W] logLx    Logarithm of the intrinsic X-ray luminosity of
                                 the star
 140-142  A3    ---   r_logLx    Reference for X-ray luminosity in refs.dat file
 144-148  F5.2  d       Prot     Rotation period of the star
 150-153  A4    ---   r_Prot     Reference for rotation period, in refs.dat file
 155-158  F4.2  Msun    M*       Mass of the star (4)
 160-163  F4.2  Rsun    R*       Radius of the star (4)
 165-169  F5.2  Lsun    L*       Bolometric luminosity of the star (4)
 171-174  I4    K       Teff     Effective temperature of the star (4)
 176-179  F4.2  ---     dcz      Height of the radiative-convective boundary
                                 (as a function of the stellar radius) (4)
 181-185  F5.2 [---]    Lx/bol   Logarithm of the X-ray to bolometric luminosity
--------------------------------------------------------------------------------
Note (1): 202 stars have no identifier; just a position.
Note (2): Taken either from known cluster distances from the literature,
     individual stellar parallaxes or fits to main-sequence models (see paper).
Note (3): Derived from spectral types where appropriate (see paper).
     Cluster stars dereddened using known cluster extinction.
Note (4): from Siess et al. (2000A&A...358..593S) model.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: refs.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  4  A4    ---     Ref       Reference code
   6- 24  A19   ---     BibCode   BibCode
  26- 56  A31   ---     Aut       Author's name
  58-131  A74   ---     Com       Comments
--------------------------------------------------------------------------------

Acknowledgements:
    Nicholas Wright, <n. j. wright at keele.ac.uk>

History:
    * 09-Feb-2012: on-line version
    * 28-Feb-2013: some names corrected
    * 03-Jun-2019: Some distances revised by the author

================================================================================
(End)     Nicholas Wright [SAO, USA], Patricia Vannier [CDS]         09-Feb-2012
