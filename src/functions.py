import at
import vt
import mt


def atNormS(km, tid, tillegg):
    return (km * at.NormKmS) + (tid * at.NormTid) + tillegg + at.NormStartS
def atNormM(km, tid, over, tillegg):
    return (km * at.NormKmM) + (tid * at.NormTid) + (over * at.NormKmOverM) + tillegg + at.NormStartM
def atNormL(km, tid, over, tillegg):
    return (km * at.NormKmL) + (tid * at.NormTid) + (over * at.NormKmOverL) + tillegg + at.NormStartL

def atHelgS(km, tid, tillegg):
    return (km * at.HelgKmS) + (tid * at.HelgTid) + tillegg + at.HelgStartS
def atHelgM(km, tid, over, tillegg):
    return (km * at.HelgKmM) + (tid * at.HelgTid) + (over * at.HelgKmOverM) + tillegg + at.HelgStartM
def atHelgL(km, tid, over, tillegg):
    return (km * at.HelgKmL) + (tid * at.HelgTid) + (over * at.HelgKmOverL) + tillegg + at.HelgStartL

def atHolyS(km, tid, tillegg):
    return (km * at.HolyKmS) + (tid * at.HolyTid) + tillegg + at.HolyStartS
def atHolyM(km, tid, over, tillegg):
    return (km * at.HolyKmM) + (tid * at.HolyTid) + (over * at.HolyKmOverM) + tillegg + at.HolyStartM
def atHolyL(km, tid, over, tillegg):
    return (km * at.HolyKmL) + (tid * at.HolyTid) + (over * at.HolyKmOverL) + tillegg + at.HolyStartL

def vtNormS(km, tid, tillegg):
    return (km * vt.NormKmS) + (tid * vt.NormTid) + tillegg + vt.NormStartS
def vtNormM(km, tid, over, tillegg):
    return (km * vt.NormKmM) + (tid * vt.NormTid) + (over * vt.NormKmOverM) + tillegg + vt.NormStartM
def vtNormL(km, tid, over, tillegg):
    return (km * vt.NormKmL) + (tid * vt.NormTid) + (over * vt.NormKmOverL) + tillegg + vt.NormStartL

def vtKvelS(km, tid, tillegg):
    return (km * vt.KvelKmS) + (tid * vt.KvelTid) + tillegg + vt.KvelStartS
def vtKvelM(km, tid, over, tillegg):
    return (km * vt.KvelKmM) + (tid * vt.KvelTid) + (over * vt.KvelKmOverM) + tillegg + vt.KvelStartM
def vtKvelL(km, tid, over, tillegg):
    return (km * vt.KvelKmL) + (tid * vt.KvelTid) + (over * vt.KvelKmOverL) + tillegg + vt.KvelStartL

def vtHelgS(km, tid, tillegg):
    return (km * vt.HelgKmS) + (tid * vt.HelgTid) + tillegg + vt.HelgStartS
def vtHelgM(km, tid, over, tillegg):
    return (km * vt.HelgKmM) + (tid * vt.HelgTid) + (over * vt.HelgKmOverM) + tillegg + vt.HelgStartM
def vtHelgL(km, tid, over, tillegg):
    return (km * vt.HelgKmL) + (tid * vt.HelgTid) + (over * vt.HelgKmOverL) + tillegg + vt.HelgStartL

def vtHolyS(km, tid, tillegg):
    return (km * vt.HolyKmS) + (tid * vt.HolyTid) + tillegg + vt.HolyStartS
def vtHolyM(km, tid, over, tillegg):
    return (km * vt.HolyKmM) + (tid * vt.HolyTid) + (over * vt.HolyKmOverM) + tillegg + vt.HolyStartM
def vtHolyL(km, tid, over, tillegg):
    return (km * vt.HolyKmL) + (tid * vt.HolyTid) + (over * vt.HolyKmOverL) + tillegg + vt.HolyStartL
