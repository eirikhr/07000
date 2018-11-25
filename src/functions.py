import at
import vt
import mt

# TODO:
# - Funksjonene til VT og MT. Se AT.
# - Bussfunksjoner til MT er ikkeeksisterende p.t.


def atNormS(km, tid, tillegg):
    resultat = (km * at.NormKmS) + (tid * at.NormTid) + tillegg + at.NormStartS
    if resultat < at.NormMinstS:
        resultat = at.NormMinstS
    return resultat


def atNormM(km, tid, tillegg):
    over = km - 30
    resultat = (km * at.NormKmM) + (tid * at.NormTid) + tillegg + at.NormStartM
    resultatlang = (30 * at.NormKmM) + (tid * at.NormTid) + (over * at.NormKmOverM) + tillegg + at.NormStartM
    if resultatlang < resultat:
        resultat = resultatlang
    if resultat < at.NormMinstM:
        resultat = at.NormMinstM
    return resultat


def atNormL(km, tid, tillegg):
    over = km - 30
    resultat = (km * at.NormKmL) + (tid * at.NormTid) + tillegg + at.NormStartL
    resultatlang = (30 * at.NormKmL) + (tid * at.NormTid) + (over * at.NormKmOverL) + tillegg + at.NormStartL
    if resultatlang < resultat:
        resultat = resultatlang
    if resultat < at.NormMinstL:
        resultat = at.NormMinstL
    return resultat


def atHelgS(km, tid, tillegg):
    resultat = (km * at.HelgKmS) + (tid * at.HelgTid) + tillegg + at.HelgStartS
    if resultat < at.HelgMinstS:
        resultat = at.HelgMinstS
    return resultat


def atHelgM(km, tid, tillegg):
    over = km - 30
    resultat = (km * at.HelgKmM) + (tid * at.HelgTid) + tillegg + at.HelgStartM
    resultatlang = (30 * at.HelgKmM) + (tid * at.HelgTid) + (over * at.HelgKmOverM) + tillegg + at.HelgStartM
    if resultatlang < resultat:
        resultat = resultatlang
    if resultat < at.HelgMinstM:
        resultat = at.HelgMinstM
    return resultat


def atHelgL(km, tid, tillegg):
    over = km - 30
    resultat = (km * at.HelgKmL) + (tid * at.HelgTid) + tillegg + at.HelgStartL
    resultatlang = (30 * at.HelgKmL) + (tid * at.HelgTid) + (over * at.HelgKmOverL) + tillegg + at.HelgStartL
    if resultatlang < resultat:
        resultat = resultatlang
    if resultat < at.HelgMinstL:
        resultat = at.HelgMinstL
    return resultat


def atHolyS(km, tid, tillegg):
    resultat = (km * at.HolyKmS) + (tid * at.HolyTid) + tillegg + at.HolyStartS
    if resultat < at.HolyMinstS:
        resultat = at.HolyMinstS
    return resultat


def atHolyM(km, tid, tillegg):
    over = km - 30
    resultat = (km * at.HolyKmM) + (tid * at.HolyTid) + tillegg + at.HolyStartM
    resultatlang = (30 * at.HolyKmM) + (tid * at.HolyTid) + (over * at.HolyKmOverM) + tillegg + at.HolyStartM
    if resultatlang < resultat:
        resultat = resultatlang
    if resultat < at.HolyMinstM:
        resultat = at.HolyMinstM
    return resultat


def atHolyL(km, tid, tillegg):
    over = km - 30
    resultat = (km * at.HolyKmL) + (tid * at.HolyTid) + tillegg + at.HolyStartL
    resultatlang = (30 * at.HolyKmL) + (tid * at.HolyTid) + (over * at.HolyKmOverL) + tillegg + at.HolyStartL
    if resultatlang < resultat:
        resultat = resultatlang
    if resultat < at.HolyMinstL:
        resultat = at.HolyMinstL
    return resultat


# VENNESLA


def vtNormS(km, tid, tillegg):
    result = (km * vt.NormKmS) + (tid * vt.NormTid) + tillegg + vt.NormStartS
    if result < vt.NormMinstS:
        result = vt.NormMinstS
    return result


def vtNormM(km, tid, tillegg):
    over = km - 30
    result = (km * vt.NormKmM) + (tid * vt.NormTid) + tillegg + vt.NormStartM
    resultlang = (30 * vt.NormKmM) + (tid * vt.NormTid) + (over * vt.NormKmOverM) + tillegg + vt.NormStartM
    if resultlang < result:
        result = resultlang
    if result < vt.NormMinstM:
        result = vt.NormMinstM
    return result


def vtNormL(km, tid, tillegg):
    over = km - 30
    result = (km * vt.NormKmL) + (tid * vt.NormTid) + tillegg + vt.NormStartL
    resultlang = (30 * vt.NormKmL) + (tid * vt.NormTid) + (over * vt.NormKmOverL) + tillegg + vt.NormStartL
    if resultlang < result:
        result = resultlang
    if result < vt.NormMinstL:
        result = vt.NormMinstL
    return result


def vtKvelS(km, tid, tillegg):
    result = (km * vt.KvelKmS) + (tid * vt.KvelTid) + tillegg + vt.KvelStartS
    if result < vt.KvelMinstS:
        result = vt.KvelMinstS
    return result


def vtKvelM(km, tid, tillegg):
    over = km - 30
    result = (km * vt.KvelKmM) + (tid * vt.KvelTid) + tillegg + vt.KvelStartM
    resultlang = (30 * vt.KvelKmM) + (tid * vt.KvelTid) + (over * vt.KvelKmOverM) + tillegg + vt.KvelStartM
    if resultlang < result:
        result = resultlang
    if result < vt.KvelMinstM:
        result = vt.KvelMinstM
    return result


def vtKvelL(km, tid, tillegg):
    over = km - 30
    result = (km * vt.KvelKmL) + (tid * vt.KvelTid) + tillegg + vt.KvelStartL
    resultlang = (30 * vt.KvelKmL) + (tid * vt.KvelTid) + (over * vt.KvelKmOverL) + tillegg + vt.KvelStartL
    if resultlang < result:
        result = resultlang
    if result < vt.KvelMinstL:
        result = vt.KvelMinstL
    return result


def vtHelgS(km, tid, tillegg):
    result = (km * vt.HelgKmS) + (tid * vt.HelgTid) + tillegg + vt.HelgStartS
    if result < vt.HelgMinstS:
        result = vt.HelgMinstS
    return result


def vtHelgM(km, tid, tillegg):
    over = km - 30
    result = (km * vt.HelgKmM) + (tid * vt.HelgTid) + tillegg + vt.HelgStartM
    resultlang = (30 * vt.HelgKmM) + (tid * vt.HelgTid) + (over * vt.HelgKmOverM) + tillegg + vt.HelgStartM
    if resultlang < result:
        result = resultlang
    if result < vt.HelgMinstM:
        result = vt.HelgMinstM
    return result


def vtHelgL(km, tid, tillegg):
    over = km - 30
    result = (km * vt.HelgKmL) + (tid * vt.HelgTid) + tillegg + vt.HelgStartL
    resultlang = (30 * vt.HelgKmL) + (tid * vt.HelgTid) + (over * vt.HelgKmOverL) + tillegg + vt.HelgStartL
    if resultlang < result:
        result = resultlang
    if result < vt.HelgMinstL:
        result = vt.HelgMinstL
    return result


def vtHolyS(km, tid, tillegg):
    result = (km * vt.HolyKmS) + (tid * vt.HolyTid) + tillegg + vt.HolyStartS
    if result < vt.HolyMinstS:
        result = vt.HolyMinstS
    return result


def vtHolyM(km, tid, tillegg):
    over = km - 30
    result = (km * vt.HolyKmM) + (tid * vt.HolyTid) + tillegg + vt.HolyStartM
    resultlang = (30 * vt.HolyKmM) + (tid * vt.HolyTid) + (over * vt.HolyKmOverM) + tillegg + vt.HolyStartM
    if resultlang < result:
        result = resultlang
    if result < vt.HolyMinstM:
        result = vt.HolyMinstM
    return result


def vtHolyL(km, tid, tillegg):
    over = km - 30
    result = (km * vt.HolyKmL) + (tid * vt.HolyTid) + tillegg + vt.HolyStartL
    resultlang = (30 * vt.HolyKmL) + (tid * vt.HolyTid) + (over * vt.HolyKmOverL) + tillegg + vt.HolyStartL
    if resultlang < result:
        result = resultlang
    if result < vt.HolyMinstL:
        result = vt.HolyMinstL
    return result


# MANDAL


def mtDagS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.DagStartS + (10 * mt.DagKmS) + (over * mt.DagKmOverS) \
                 + (frem * mt.DagTilkS) + (tid * mt.DagTid) + tillegg
        return result
    else:
        result = mt.DagStartS + (km * mt.DagKmS) + (frem * mt.DagTilkS) + (tid * mt.DagTid) + tillegg
        if result < mt.DagMinstS:
            result = mt.DagMinstS
        return result


def mtDagFremS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.DagFremS + (10 * mt.DagKmS) + (over * mt.DagKmOverS) \
                 + (frem * mt.DagTilkS) + (tid * mt.DagTid) + tillegg
        return result
    else:
        result = mt.DagFremS + (km * mt.DagKmS) + (frem * mt.DagTilkS) + (tid * mt.DagTid) + tillegg
        if result < mt.DagMinstS:
            result = mt.DagMinstS
        return result


def mtKvelS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.KvelStartS + (10 * mt.KvelKmS) + (over * mt.KvelKmOverS) \
                 + (frem * mt.KvelTilkS) + (tid * mt.KvelTid) + tillegg
        return result
    else:
        result = mt.KvelStartS + (km * mt.KvelKmS) + (frem * mt.KvelTilkS) + (tid * mt.KvelTid) + tillegg
        if result < mt.KvelMinstS:
            result = mt.KvelMinstS
        return result


def mtKvelFremS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.KvelFremS + (10 * mt.KvelKmS) + (over * mt.KvelKmOverS) \
                 + (frem * mt.KvelTilkS) + (tid * mt.KvelTid) + tillegg
        return result
    else:
        result = mt.KvelFremS + (km * mt.KvelKmS) + (frem * mt.KvelTilkS) + (tid * mt.KvelTid) + tillegg
        if result < mt.KvelMinstS:
            result = mt.KvelMinstS
        return result


def mtLordS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.LordStartS + (10 * mt.LordKmS) + (over * mt.LordKmOverS) \
                 + (frem * mt.LordTilkS) + (tid * mt.LordTid) + tillegg
        return result
    else:
        result = mt.LordStartS + (km * mt.LordKmS) + (frem * mt.LordTilkS) + (tid * mt.LordTid) + tillegg
        if result < mt.LordMinstS:
            result = mt.LordMinstS
        return result


def mtLordFremS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.LordFremS + (10 * mt.LordKmS) + (over * mt.LordKmOverS) \
                 + (frem * mt.LordTilkS) + (tid * mt.LordTid) + tillegg
        return result
    else:
        result = mt.LordFremS + (km * mt.LordKmS) + (frem * mt.LordTilkS) + (tid * mt.LordTid) + tillegg
        if result < mt.LordMinstS:
            result = mt.LordMinstS
        return result


def mtHelgS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HelgStartS + (10 * mt.HelgKmS) + (over * mt.HelgKmOverS) \
                 + (frem * mt.HelgTilkS) + (tid * mt.HelgTid) + tillegg
        return result
    else:
        result = mt.HelgStartS + (km * mt.HelgKmS) + (frem * mt.HelgTilkS) + (tid * mt.HelgTid) + tillegg
        if result < mt.HelgMinstS:
            result = mt.HelgMinstS
        return result


def mtHelgFremS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HelgFremS + (10 * mt.HelgKmS) + (over * mt.HelgKmOverS) \
                 + (frem * mt.HelgTilkS) + (tid * mt.HelgTid) + tillegg
        return result
    else:
        result = mt.HelgFremS + (km * mt.HelgKmS) + (frem * mt.HelgTilkS) + (tid * mt.HelgTid) + tillegg
        if result < mt.HelgMinstS:
            result = mt.HelgMinstS
        return result


def mtHolyS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HolyStartS + (10 * mt.HolyKmS) + (over * mt.HolyKmOverS) \
                 + (frem * mt.HolyTilkS) + (tid * mt.HolyTid) + tillegg
        return result
    else:
        result = mt.HolyStartS + (km * mt.HolyKmS) + (frem * mt.HolyTilkS) + (tid * mt.HolyTid) + tillegg
        if result < mt.HolyMinstS:
            result = mt.HolyMinstS
        return result


def mtHolyFremS(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HolyFremS + (10 * mt.HolyKmS) + (over * mt.HolyKmOverS) \
                 + (frem * mt.HolyTilkS) + (tid * mt.HolyTid) + tillegg
        return result
    else:
        result = mt.HolyFremS + (km * mt.HolyKmS) + (frem * mt.HolyTilkS) + (tid * mt.HolyTid) + tillegg
        if result < mt.HolyMinstS:
            result = mt.HolyMinstS
        return result


def mtDagM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.DagStartM + (10 * mt.DagKmM) + (over * mt.DagKmOverM) \
                 + (frem * mt.DagTilkM) + (tid * mt.DagTid) + tillegg
        return result
    else:
        result = mt.DagStartM + (km * mt.DagKmM) + (frem * mt.DagTilkM) + (tid * mt.DagTid) + tillegg
        if result < mt.DagMinstM:
            result = mt.DagMinstM
        return result


def mtDagFremM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.DagFremM + (10 * mt.DagKmM) + (over * mt.DagKmOverM) \
                 + (frem * mt.DagTilkM) + (tid * mt.DagTid) + tillegg
        return result
    else:
        result = mt.DagFremM + (km * mt.DagKmM) + (frem * mt.DagTilkM) + (tid * mt.DagTid) + tillegg
        if result < mt.DagMinstM:
            result = mt.DagMinstM
        return result


def mtKvelM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.KvelStartM + (10 * mt.KvelKmM) + (over * mt.KvelKmOverM) \
                 + (frem * mt.KvelTilkM) + (tid * mt.KvelTid) + tillegg
        return result
    else:
        result = mt.KvelStartM + (km * mt.KvelKmM) + (frem * mt.KvelTilkM) + (tid * mt.KvelTid) + tillegg
        if result < mt.KvelMinstM:
            result = mt.KvelMinstM
        return result


def mtKvelFremM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.KvelFremM + (10 * mt.KvelKmM) + (over * mt.KvelKmOverM) \
                 + (frem * mt.KvelTilkM) + (tid * mt.KvelTid) + tillegg
        return result
    else:
        result = mt.KvelFremM + (km * mt.KvelKmM) + (frem * mt.KvelTilkM) + (tid * mt.KvelTid) + tillegg
        if result < mt.KvelMinstM:
            result = mt.KvelMinstM
        return result


def mtLordM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.LordStartM + (10 * mt.LordKmM) + (over * mt.LordKmOverM) \
                 + (frem * mt.LordTilkM) + (tid * mt.LordTid) + tillegg
        return result
    else:
        result = mt.LordStartM + (km * mt.LordKmM) + (frem * mt.LordTilkM) + (tid * mt.LordTid) + tillegg
        if result < mt.LordMinstM:
            result = mt.LordMinstM
        return result


def mtLordFremM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.LordFremM + (10 * mt.LordKmM) + (over * mt.LordKmOverM) \
                 + (frem * mt.LordTilkM) + (tid * mt.LordTid) + tillegg
        return result
    else:
        result = mt.LordFremM + (km * mt.LordKmM) + (frem * mt.LordTilkM) + (tid * mt.LordTid) + tillegg
        if result < mt.LordMinstM:
            result = mt.LordMinstM
        return result


def mtHelgM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HelgStartM + (10 * mt.HelgKmM) + (over * mt.HelgKmOverM) \
                 + (frem * mt.HelgTilkM) + (tid * mt.HelgTid) + tillegg
        return result
    else:
        result = mt.HelgStartM + (km * mt.HelgKmM) + (frem * mt.HelgTilkM) + (tid * mt.HelgTid) + tillegg
        if result < mt.HelgMinstM:
            result = mt.HelgMinstM
        return result


def mtHelgFremM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HelgFremM + (10 * mt.HelgKmM) + (over * mt.HelgKmOverM) \
                 + (frem * mt.HelgTilkM) + (tid * mt.HelgTid) + tillegg
        return result
    else:
        result = mt.HelgFremM + (km * mt.HelgKmM) + (frem * mt.HelgTilkM) + (tid * mt.HelgTid) + tillegg
        if result < mt.HelgMinstM:
            result = mt.HelgMinstM
        return result


def mtHolyM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HolyStartM + (10 * mt.HolyKmM) + (over * mt.HolyKmOverM) \
                 + (frem * mt.HolyTilkM) + (tid * mt.HolyTid) + tillegg
        return result
    else:
        result = mt.HolyStartM + (km * mt.HolyKmM) + (frem * mt.HolyTilkM) + (tid * mt.HolyTid) + tillegg
        if result < mt.HolyMinstM:
            result = mt.HolyMinstM
        return result


def mtHolyFremM(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HolyFremM + (10 * mt.HolyKmM) + (over * mt.HolyKmOverM) \
                 + (frem * mt.HolyTilkM) + (tid * mt.HolyTid) + tillegg
        return result
    else:
        result = mt.HolyFremM + (km * mt.HolyKmM) + (frem * mt.HolyTilkM) + (tid * mt.HolyTid) + tillegg
        if result < mt.HolyMinstM:
            result = mt.HolyMinstM
        return result


def mtDagL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.DagStartL + (10 * mt.DagKmL) + (over * mt.DagKmOverL) \
                 + (frem * mt.DagTilkL) + (tid * mt.DagTid) + tillegg
        return result
    else:
        result = mt.DagStartL + (km * mt.DagKmL) + (frem * mt.DagTilkL) + (tid * mt.DagTid) + tillegg
        if result < mt.DagMinstL:
            result = mt.DagMinstL
        return result


def mtDagFremL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.DagFremL + (10 * mt.DagKmL) + (over * mt.DagKmOverL) \
                 + (frem * mt.DagTilkL) + (tid * mt.DagTid) + tillegg
        return result
    else:
        result = mt.DagFremL + (km * mt.DagKmL) + (frem * mt.DagTilkL) + (tid * mt.DagTid) + tillegg
        if result < mt.DagMinstL:
            result = mt.DagMinstL
        return result


def mtKvelL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.KvelStartL + (10 * mt.KvelKmL) + (over * mt.KvelKmOverL) \
                 + (frem * mt.KvelTilkL) + (tid * mt.KvelTid) + tillegg
        return result
    else:
        result = mt.KvelStartL + (km * mt.KvelKmL) + (frem * mt.KvelTilkL) + (tid * mt.KvelTid) + tillegg
        if result < mt.KvelMinstL:
            result = mt.KvelMinstL
        return result


def mtKvelFremL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.KvelFremL + (10 * mt.KvelKmL) + (over * mt.KvelKmOverL) \
                 + (frem * mt.KvelTilkL) + (tid * mt.KvelTid) + tillegg
        return result
    else:
        result = mt.KvelFremL + (km * mt.KvelKmL) + (frem * mt.KvelTilkL) + (tid * mt.KvelTid) + tillegg
        if result < mt.KvelMinstL:
            result = mt.KvelMinstL
        return result


def mtLordL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.LordStartL + (10 * mt.LordKmL) + (over * mt.LordKmOverL) \
                 + (frem * mt.LordTilkL) + (tid * mt.LordTid) + tillegg
        return result
    else:
        result = mt.LordStartL + (km * mt.LordKmL) + (frem * mt.LordTilkL) + (tid * mt.LordTid) + tillegg
        if result < mt.LordMinstL:
            result = mt.LordMinstL
        return result


def mtLordFremL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.LordFremL + (10 * mt.LordKmL) + (over * mt.LordKmOverL) \
                 + (frem * mt.LordTilkL) + (tid * mt.LordTid) + tillegg
        return result
    else:
        result = mt.LordFremL + (km * mt.LordKmL) + (frem * mt.LordTilkL) + (tid * mt.LordTid) + tillegg
        if result < mt.LordMinstL:
            result = mt.LordMinstL
        return result


def mtHelgL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HelgStartL + (10 * mt.HelgKmL) + (over * mt.HelgKmOverL) \
                 + (frem * mt.HelgTilkL) + (tid * mt.HelgTid) + tillegg
        return result
    else:
        result = mt.HelgStartL + (km * mt.HelgKmL) + (frem * mt.HelgTilkL) + (tid * mt.HelgTid) + tillegg
        if result < mt.HelgMinstL:
            result = mt.HelgMinstL
        return result


def mtHelgFremL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HelgFremL + (10 * mt.HelgKmL) + (over * mt.HelgKmOverL) \
                 + (frem * mt.HelgTilkL) + (tid * mt.HelgTid) + tillegg
        return result
    else:
        result = mt.HelgFremL + (km * mt.HelgKmL) + (frem * mt.HelgTilkL) + (tid * mt.HelgTid) + tillegg
        if result < mt.HelgMinstL:
            result = mt.HelgMinstL
        return result


def mtHolyL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HolyStartL + (10 * mt.HolyKmL) + (over * mt.HolyKmOverL) \
                 + (frem * mt.HolyTilkL) + (tid * mt.HolyTid) + tillegg
        return result
    else:
        result = mt.HolyStartL + (km * mt.HolyKmL) + (frem * mt.HolyTilkL) + (tid * mt.HolyTid) + tillegg
        if result < mt.HolyMinstL:
            result = mt.HolyMinstL
        return result


def mtHolyFremL(km, tid, frem, tillegg):
    over = km - 10
    if km > 10:
        result = mt.HolyFremL + (10 * mt.HolyKmL) + (over * mt.HolyKmOverL) \
                 + (frem * mt.HolyTilkL) + (tid * mt.HolyTid) + tillegg
        return result
    else:
        result = mt.HolyFremL + (km * mt.HolyKmL) + (frem * mt.HolyTilkL) + (tid * mt.HolyTid) + tillegg
        if result < mt.HolyMinstL:
            result = mt.HolyMinstL
        return result

