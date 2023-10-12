J/A+A/556/A26  Arches cluster: IR phot., extinction and masses  (Habibi+, 2013)
================================================================================
The Arches cluster out to its tidal radius: dynamical mass segregation and the
effect of the extinction law on the stellar mass function.
    Habibi M., Stolte A., Brandner W., Hussmann B., Motohara K.
   <Astron. Astrophys. 556, A26 (2013)>
   =2013A&A...556A..26H
================================================================================
ADC_Keywords: Clusters, open ; Photometry, infrared ; Stars, masses
Keywords: Galaxy: center, open clusters and associations -
          individual: Arches cluster, stellar dynamics, extinction map -
          stars: mass function, luminosity function - stars: early-type -
          infrared: stars - instrumentation: adaptive optics

Abstract:
    The Galactic Center is the most active site of star formation in the
    Milky Way Galaxy, where particularly high-mass stars have formed very
    recently and are still forming today. However, since we are looking at
    the Galactic Center through the Galactic disk, knowledge of extinction
    is crucial to study this region. The Arches cluster is a young,
    massive starburst cluster near the Galactic Center. We observed the
    Arches cluster out to its tidal radius using Ks-band imaging obtained
    with NAOS/CONICA at the VLT combined with Subaro/Cisco J-band data to
    gain a full understanding of the cluster mass distribution. We show
    that the determination of the mass of the most massive star in the
    Arches cluster, which had been used in previous studies to establish
    an upper-mass limit for the star formation process in the Milky Way,
    strongly depends on the assumed slope of the extinction law. Assuming
    the two regimes of widely used infrared extinction laws, we show that
    the difference can reach up to 30% for individually derived stellar
    masses and {Delta}AKs~1 magnitude in acquired Ks-band extinction,
    while the present mass function slope changes by ~0.17dex. The
    present-day mass function slope derived assuming the Nishiyama et al.
    (2009) extinction law increases from a flat slope of
    {alpha}-Nishi=-1.50+/-0.35 in the core (r<0.2pc) to
    {alpha}-Nishi=-2.21+/-0.27 in the intermediate annulus (0.2<r<0.4pc),
    where the Salpeter slope is -2.3. The present-day mass function
    steepens to {alpha}-Nishi=-3.21+/-0.30 in the outer annulus
    (0.4<r<1.5pc), indicating that the outer cluster region is depleted of
    high mass stars. This picture is consistent with mass segregation due
    to the dynamical evolution of the cluster.

Description:
    We observed the Arches cluster out to its tidal radius using Ks-band
    and H-band imaging obtained on June 6-10 2008 with NAOS/CONICA at the
    VLT combined with Subaro/Cisco J-band data to gain a full
    understanding of the cluster mass distribution. The acquired Ks-band
    images cover four fields of 27.8*27.8(arcsec) each, provided by the
    medium resolution camera (S27) with a pixel scale of 0.027(arcsec).
    During the Ks-band observations, the natural visual seeing varied from
    0.61" to 0.98". We achieved typical spatial resolutions of
    0.081-0.135(arcsec) on individual frames using this AO setup.
    Seeing-limited J-band observations, on July 17, 2000, were performed
    with the CISCO spectrograph and camera which provided a pixel scale of
    0.116(arcsec) and a field of view of 2*2(arcmin). An average seeing of
    0.49(arcsec) resulted into a Full Width at Half Maximum (FWHM) of the
    point-spread function (PSF) of 0.39(arcsec) on the combined image. The
    catalogue includes derived infrared-photometry in J, H and Ks bands as
    well as derived individual extinction value and stellar masses.

    We used the NAOS-CONICA observations obtained in March 2002 in the
    central part of the Arches cluster to cover the whole cluster area.

Objects:
    -------------------------------------------------------------
       RA   (2000)   DE      Designation(s)
    -------------------------------------------------------------
    17 45 50.5   -28 49 28   Arches cluster = NAME ARCHES CLUSTER
    -------------------------------------------------------------

File Summary:
--------------------------------------------------------------------------------
 FileName   Lrecl  Records   Explanations
--------------------------------------------------------------------------------
ReadMe         80        .   This file
table5.dat    101     3351   Photometry, mass and extinction in Arches cluster
--------------------------------------------------------------------------------

See also:
  II/319 : UKIDSS-DR9 LAS, GCS and DXS Surveys (Lawrence+ 2012)
  J/ApJ/581/258  : Infrared photometry in the Arches Cluster (Figer+, 2002)
  J/MNRAS/371/38 : X-ray observations of the Galaxy center (Wang+, 2006)
  J/ApJ/670/1115 : IRS spectra at 38 positions in GC (Simpson+, 2007)
  J/A+A/501/563  : HKs photometry in the Arches cluster (Espinoza+, 2009)
  J/ApJ/718/810  : Astrometry & photometry in the Arches cluster (Stolte+, 2010)

Byte-by-byte Description of file: table5.dat
--------------------------------------------------------------------------------
   Bytes Format Units   Label    Explanations
--------------------------------------------------------------------------------
   1-  4  I4    ---     Seq      Sequential number
   6- 12  F7.3  arcsec  oRA      Right ascension offset from the reference
                                  star, J2000 (1)
  14- 20  F7.3  arcsec  oDE      Declination offset from the reference
                                  star, J2000 (1)
  22- 27  F6.3  mag     AKs(RL)  ?=-9 Ks-band extinction applying the RL-EL (2)
  29- 34  F6.3  mag     AKs(N)   ?=-9 Ks-band extinction applying the N-EL (2)
  36- 43  F8.3  Msun    Mi(RL)   ?=-999 Initial mass applying the RL-EL (2) (3)
  45- 51  F7.3  Msun    M(RL)    ?=-99 Present mass applying the RL-EL (2) (3)
  53- 59  F7.3  Msun    Mi(N)    ?=-99 Initial mass applying the N-EL (2) (3)
  61- 67  F7.3  Msun    M(N)     ?=-99 Present mass applying the N-EL (2) (3)
  69- 75  F7.3  mag     Jmag     [0/23.1]?=-99 J-band brightness
  77- 83  F7.3  mag     Hmag     [10.9/23.6]?=-99 H-band brightness
  85- 90  F6.3  mag     Ksmag    [0/33.4]? Ks-band brightness
  92- 97  F6.3  mag     A(Ks)    [0/0.442]?=-9.000 estimated Ks-band extinction
      99  I1    ---     F        [1/5] Cluster field in which the source is
                                       located
     101  I1    ---     Mm       [0/1] Cluster members (1), others (0)
--------------------------------------------------------------------------------
Note (1): Position offsets are calculated  with respect to reference star
     which is the source with ID 1, at 17:45:50.046-28:49:23.62 (J2000).
Note (2): Masses are derived by comparing our observations against the Geneva
     isochrone with solar metallicity located at the GC distance of 8kpc.
Note (3): RL-EL stands for Rieke and Lebofsky (1985ApJ...288..618R) Extinction
     Law, and N-EL stands for Nishiyama et al (2009ApJ...696.1407N) extinction
     law.
--------------------------------------------------------------------------------

Acknowledgements:
    Maryam Habibi, mhabibi(at)astro.uni-bonn.de

================================================================================
(End)   Maryam Habibi [Bonn Univ., Germany], Patricia Vannier [CDS]  21-May-2013
