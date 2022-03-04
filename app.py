from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/tonelada-tonelada/<string:tonelada>")
def get_datosTT(tonelada):
    tonelada = float(tonelada)
    pesoTT = tonelada
    return jsonify({ "pesoTT" : pesoTT})

@app.route("/tonelada-kilogramo/<string:tonelada>")
def get_datosTK(tonelada):
    tonelada = float(tonelada)
    pesoTK = tonelada*10
    return jsonify({ "pesoTK" : pesoTK})

@app.route("/tonelada-hectogramo/<string:tonelada>")
def get_datosTH(tonelada):
    tonelada = float(tonelada)
    pesoTH = tonelada*100
    return jsonify({ "pesoTH" : pesoTH})

@app.route("/tonelada-decagramo/<string:tonelada>")
def get_datosTD(tonelada):
    tonelada = float(tonelada)
    pesoTD = tonelada*1000
    return jsonify({ "pesoTD" : pesoTD})    

@app.route("/tonelada-gramo/<string:tonelada>")
def get_datosTg(tonelada):
    tonelada = float(tonelada)
    pesoTg = tonelada*10000
    return jsonify({ "pesoTg" : pesoTg})

@app.route("/tonelada-decigramo/<string:tonelada>")
def get_datosTd(tonelada):
    tonelada = float(tonelada)
    pesoTd = tonelada*100000
    return jsonify({ "pesoTd" : pesoTd})


@app.route("/tonelada-centigramo/<string:tonelada>")
def get_datosTc(tonelada):
    tonelada = float(tonelada)
    pesoTc = tonelada*1000000
    return jsonify({ "pesoTc" : pesoTc})


@app.route("/tonelada-miligramo/<string:tonelada>")
def get_datosTm(tonelada):
    tonelada = float(tonelada)
    pesoTm = tonelada*10000000
    return jsonify({ "pesoTm" : pesoTm})


@app.route("/tonelada-microgramo/<string:tonelada>")
def get_datosTmi(tonelada):
    tonelada = float(tonelada)
    pesoTmi = tonelada*100000000
    return jsonify({ "pesoTmi" : pesoTmi})


@app.route("/tonelada-nanogramo/<string:tonelada>")
def get_datosTn(tonelada):
    tonelada = float(tonelada)
    pesoTn = tonelada*1000000000
    return jsonify({ "pesoTn" : pesoTn})        

@app.route("/kilogramo-tonelada/<string:kilogramo>")
def get_datosKT(kilogramo):
    kilogramo = float(kilogramo)
    pesoKT = kilogramo/10
    return jsonify({ "pesoKT" : pesoKT})  

@app.route("/kilogramo-kilogramo/<string:kilogramo>")
def get_datosKK(kilogramo):
    kilogramo = float(kilogramo)
    pesoKK = kilogramo
    return jsonify({ "pesoKK" : pesoKK})                

@app.route("/kilogramo-hectogramo/<string:kilogramo>")
def get_datosKH(kilogramo):
    kilogramo = float(kilogramo)
    pesoKH = kilogramo*10
    return jsonify({ "pesoKH" : pesoKH})

@app.route("/kilograma-decagramo/<string:kilogramo>")
def get_datosKD(kilogramo):
    kilogramo = float(kilogramo)
    pesoKD = kilogramo*100
    return jsonify({ "pesoKD" : pesoKD})

@app.route("/kilograma-gramo/<string:kilogramo>")
def get_datosKg(kilogramo):
    kilogramo = float(kilogramo)
    pesoKg = kilogramo*1000
    return jsonify({ "pesoKg" : pesoKg})

@app.route("/kilograma-decigramo/<string:kilogramo>")
def get_datosKd(kilogramo):
    kilogramo = float(kilogramo)
    pesoKd = kilogramo*10000
    return jsonify({ "pesoKd" : pesoKd})  

@app.route("/kilograma-centigramo/<string:kilogramo>")
def get_datosKc(kilogramo):
    kilogramo = float(kilogramo)
    pesoKc = kilogramo*100000
    return jsonify({ "pesoKc" : pesoKc})

@app.route("/kilograma-miligramo/<string:kilogramo>")
def get_datosKm(kilogramo):
    kilogramo = float(kilogramo)
    pesoKm = kilogramo*1000000
    return jsonify({ "pesoKm" : pesoKm})

@app.route("/kilograma-microgramo/<string:kilogramo>")
def get_datosKmi(kilogramo):
    kilogramo = float(kilogramo)
    pesoKmi = kilogramo*10000000
    return jsonify({ "pesoKmi" : pesoKmi})

@app.route("/kilograma-nanogramo/<string:kilogramo>")
def get_datosKn(kilogramo):
    kilogramo = float(kilogramo)
    pesoKn = kilogramo*100000000
    return jsonify({ "pesoKn" : pesoKn})                  


@app.route("/hectogramo-tonelada/<string:hectogramo>")
def get_datosHT(hectogramo):
    hectogramo = float(hectogramo)
    pesoHT = hectogramo/100
    return jsonify({ "pesoHT" : pesoHT})


@app.route("/hectogramo-kilogramo/<string:hectogramo>")
def get_datosHK(hectogramo):
    hectogramo = float(hectogramo)
    pesoHK = hectogramo/10
    return jsonify({ "pesoHK" : pesoHK})   

@app.route("/hectogramo-hectogramo/<string:hectogramo>")
def get_datosHH(hectogramo):
    hectogramo = float(hectogramo)
    pesoHH = hectogramo
    return jsonify({ "pesoHH" : pesoHH})    

@app.route("/hectogramo-decagramo/<string:hectogramo>")
def get_datosHD(hectogramo):
    hectogramo = float(hectogramo)
    pesoHD = hectogramo*10
    return jsonify({ "pesoHD" : pesoHD})

@app.route("/hectogramo-gramo/<string:hectogramo>")
def get_datosHg(hectogramo):
    hectogramo = float(hectogramo)
    pesoHg = hectogramo*100
    return jsonify({ "pesoHg" : pesoHg})

@app.route("/hectogramo-decigramo/<string:hectogramo>")
def get_datoHd(hectogramo):
    hectogramo = float(hectogramo)
    pesoHd = hectogramo*1000
    return jsonify({ "pesoHd" : pesoHd})    

@app.route("/hectogramo-centigramo/<string:hectogramo>")
def get_datosHc(hectogramo):
    hectogramo = float(hectogramo)
    pesoHc = hectogramo*10000
    return jsonify({ "pesoHc" : pesoHc})

@app.route("/hectogramo-miligramo/<string:hectogramo>")
def get_datosHm(hectogramo):
    hectogramo = float(hectogramo)
    pesoHm = hectogramo*100000
    return jsonify({ "pesoHm" : pesoHm})

@app.route("/hectogramo-microgramo/<string:hectogramo>")
def get_datosHmi(hectogramo):
    hectogramo = float(hectogramo)
    pesoHmi = hectogramo*1000000
    return jsonify({ "pesoHmi" : pesoHmi})

@app.route("/hectogramo-nanogramo/<string:hectogramo>")
def get_datosHn(hectogramo):
    hectogramo = float(hectogramo)
    pesoHn = hectogramo*10000000
    return jsonify({ "pesoHn" : pesoHn})            

@app.route("/decagramo-tonelada/<string:decagramo>")
def get_datosDT(decagramo):
    decagramo = float(decagramo)
    pesoDT = decagramo/1000
    return jsonify({ "pesoDT" : pesoDT})


@app.route("/decagramo-kilogramo/<string:decagramo>")
def get_datosDK(decagramo):
    decagramo = float(decagramo)
    pesoDK = decagramo/100
    return jsonify({ "pesoDK" : pesoDK})

@app.route("/decagramo-hectogramo/<string:decagramo>")
def get_datosDH(decagramo):
    decagramo = float(decagramo)
    pesoDH = decagramo/10
    return jsonify({ "pesoDH" : pesoDH})

@app.route("/decagramo-decagramo/<string:decagramo>")
def get_datosDD(decagramo):
    decagramo = float(decagramo)
    pesoDD = decagramo
    return jsonify({ "pesoDD" : pesoDD})

@app.route("/decagramo-gramo/<string:decagramo>")
def get_datosDg(decagramo):
    decagramo = float(decagramo)
    pesoDg = decagramo*10
    return jsonify({ "pesoDg" : pesoDg})

@app.route("/decagramo-decigramo/<string:decagramo>")
def get_datosDd(decagramo):
    decagramo = float(decagramo)
    pesoDd = decagramo*100
    return jsonify({ "pesoDd" : pesoDd})

@app.route("/decagramo-centigramo/<string:decagramo>")
def get_datosDc(decagramo):
    decagramo = float(decagramo)
    pesoDc = decagramo*1000
    return jsonify({ "pesoDc" : pesoDc})


@app.route("/decagramo-miligramo/<string:decagramo>")
def get_datosDm(decagramo):
    decagramo = float(decagramo)
    pesoDm = decagramo*10000
    return jsonify({ "pesoDm" : pesoDm})

@app.route("/decagramo-microgramo/<string:decagramo>")
def get_datosDmi(decagramo):
    decagramo = float(decagramo)
    pesoDmi = decagramo*100000
    return jsonify({ "pesoDmi" : pesoDmi})

@app.route("/decagramo-nanogramo/<string:decagramo>")
def get_datosDn(decagramo):
    decagramo = float(decagramo)
    pesoDn = decagramo*1000000
    return jsonify({ "pesoDn" : pesoDn})   

@app.route("/gramo-tonelada/<string:gramo>")
def get_datos_gT(gramo):
    gramo = float(gramo)
    peso_gT = gramo/10000
    return jsonify({ "peso_gT" : peso_gT})

@app.route("/gramo-kilogramo/<string:gramo>")
def get_datos_gK(gramo):
    gramo = float(gramo)
    peso_gK = gramo/1000
    return jsonify({ "peso_gK" : peso_gK})

@app.route("/gramo-hectogramo/<string:gramo>")
def get_datos_gH(gramo):
    gramo = float(gramo)
    peso_gH = gramo/100
    return jsonify({ "peso_gH" : peso_gH})

@app.route("/gramo-decagramo/<string:gramo>")
def get_datos_gD(gramo):
    gramo = float(gramo)
    peso_gD = gramo/10
    return jsonify({ "peso_gD" : peso_gD})     

@app.route("/gramo-gramo/<string:gramo>")
def get_datos_gg(gramo):
    gramo = float(gramo)
    peso_gg = gramo
    return jsonify({ "peso_gg" : peso_gg})       

@app.route("/gramo-decigramo/<string:gramo>")
def get_datos_gd(gramo):
    gramo = float(gramo)
    peso_gd = gramo*10
    return jsonify({ "peso_gd" : peso_gd})

@app.route("/gramo-centigramo/<string:gramo>")
def get_datos_gc(gramo):
    gramo = float(gramo)
    peso_gc = gramo*100
    return jsonify({ "peso_gc" : peso_gc})

@app.route("/gramo-miligramo/<string:gramo>")
def get_datos_gm(gramo):
    gramo = float(gramo)
    peso_gm = gramo*1000
    return jsonify({ "peso_gm" : peso_gm})

@app.route("/gramo-microgramo/<string:gramo>")
def get_datos_gmi(gramo):
    gramo = float(gramo)
    peso_gmi = gramo*10000
    return jsonify({ "peso_gmi" : peso_gmi}) 

@app.route("/gramo-nanogramo/<string:gramo>")
def get_datos_gn(gramo):
    gramo = float(gramo)
    peso_gn = gramo*100000
    return jsonify({ "peso_gn" : peso_gn})         

@app.route("/decigramo-tonelada/<string:decigramo>")
def get_datos_dT(decigramo):
    decigramo = float(decigramo)
    peso_dT = decigramo/10000
    return jsonify({ "peso_dT" : peso_dT})

@app.route("/decigramo-hectogramo/<string:decigramo>")
def get_datos_dH(decigramo):
    decigramo = float(decigramo)
    peso_dH = decigramo/1000
    return jsonify({ "peso_dH" : peso_dH})

@app.route("/decigramo-decagramo/<string:decigramo>")
def get_datos_dD(decigramo):
    decigramo = float(decigramo)
    peso_dD = decigramo/100
    return jsonify({ "peso_dD" : peso_dD})

@app.route("/decigramo-gramo/<string:decigramo>")
def get_datos_dg(decigramo):
    decigramo = float(decigramo)
    peso_dg = decigramo/10
    return jsonify({ "peso_dg" : peso_dg})

@app.route("/decigramo-decigramo/<string:decigramo>")
def get_datos_dd(decigramo):
    peso_dd = float(decigramo)
    return jsonify({ "peso_dd" : peso_dd})

@app.route("/decigramo-centigramo/<string:decigramo>")
def get_datos_dc(decigramo):
    decigramo = float(decigramo)
    peso_dc = decigramo*10
    return jsonify({ "peso_dc" : peso_dc})

@app.route("/decigramo-miligramo/<string:decigramo>")
def get_datos_dm(decigramo):
    decigramo = float(decigramo)
    peso_dm = decigramo*100
    return jsonify({ "peso_dm" : peso_dm})

@app.route("/decigramo-microgramo/<string:decigramo>")
def get_datos_dmi(decigramo):
    decigramo = float(decigramo)
    peso_dmi = decigramo*1000
    return jsonify({ "peso_dmi" : peso_dmi})


@app.route("/decigramo-nanogramo/<string:centigramo>")
def get_datos_dn(centigramo):
    centigramo = float(centigramo)
    peso_dn = centigramo*10000
    return jsonify({ "peso_dn" : peso_dn})

@app.route("/centigramo-tonelada/<string:centigramo>")
def get_datos_cT(centigramo):
    centigramo = float(centigramo)
    peso_cT = centigramo/1000000
    return jsonify({ "peso_cT" : peso_cT})

@app.route("/centigramo-kilogramo/<string:centigramo>")
def get_datos_cK(centigramo):
    centigramo = float(centigramo)
    peso_cK = centigramo/100000
    return jsonify({ "peso_cK" : peso_cK})

@app.route("/centigramo-hectogramo/<string:centigramo>")
def get_datos_cH(centigramo):
    centigramo = float(centigramo)
    peso_cH = centigramo/10000
    return jsonify({ "peso_cH" : peso_cH})

@app.route("/centigramo-decagramo/<string:centigramo>")
def get_datos_cD(centigramo):
    centigramo = float(centigramo)
    peso_cD = centigramo/1000
    return jsonify({ "peso_cD" : peso_cD})

@app.route("/centigramo-gramo/<string:centigramo>")
def get_datos_cg(centigramo):
    centigramo = float(centigramo)
    peso_cg = centigramo/100
    return jsonify({ "peso_cg" : peso_cg})

@app.route("/centigramo-decigramo/<string:centigramo>")
def get_datos_cd(centigramo):
    centigramo = float(centigramo)
    peso_cd = centigramo/10
    return jsonify({ "peso_cd" : peso_cd})

@app.route("/centigramo-centigramo/<string:centigramo>")
def get_datos_cc(centigramo):
    peso_cc = float(centigramo)
    return jsonify({ "peso_cc" : peso_cc})

@app.route("/centigramo-microgramo/<string:centigramo>")
def get_datos_cmi(centigramo):
    centigramo = float(centigramo)
    peso_cmi = centigramo*10
    return jsonify({ "peso_cmi" : peso_cmi})

@app.route("/centigramo-nanogramo/<string:centigramo>")
def get_datos_cn(centigramo):
    centigramo = float(centigramo)
    peso_cn = centigramo*100
    return jsonify({ "peso_cn" : peso_cn})

@app.route("/miligramo-tonelada/<string:miligramo>")
def get_datos_mT(miligramo):
    miligramo = float(miligramo)
    peso_mT = miligramo/10000000
    return jsonify({ "peso_mT" : peso_mT})

@app.route("/miligramo-kilogramo/<string:miligramo>")
def get_datos_mK(miligramo):
    miligramo = float(miligramo)
    peso_mK = miligramo/1000000
    return jsonify({ "peso_mK" : peso_mK}) 

@app.route("/miligramo-hectogramo/<string:miligramo>")
def get_datos_mH(miligramo):
    miligramo = float(miligramo)
    peso_mH = miligramo/100000
    return jsonify({ "peso_mH" : peso_mH})  

@app.route("/miligramo-decagramo/<string:miligramo>")
def get_datos_mD(miligramo):
    miligramo = float(miligramo)
    peso_mD = miligramo/10000
    return jsonify({ "peso_mD" : peso_mD}) 

@app.route("/miligramo-gramo/<string:miligramo>")
def get_datos_mg(miligramo):
    miligramo = float(miligramo)
    peso_mg = miligramo/1000
    return jsonify({ "peso_mg" : peso_mg}) 

@app.route("/miligramo-decigramo/<string:miligramo>")
def get_datos_md(miligramo):
    miligramo = float(miligramo)
    peso_md = miligramo/100
    return jsonify({ "peso_md" : peso_md}) 

@app.route("/miligramo-centigramo/<string:miligramo>")
def get_datos_mc(miligramo):
    miligramo = float(miligramo)
    peso_mc = miligramo/10
    return jsonify({ "peso_mc" : peso_mc}) 

@app.route("/miligramo-miligramo/<string:miligramo>")
def get_datos_mm(miligramo):
    peso_mm = float(miligramo)
    return jsonify({ "peso_mm" : peso_mm})  

@app.route("/miligramo-microgramo/<string:miligramo>")
def get_datos_mmi(miligramo):
    miligramo = float(miligramo)
    peso_mmi = miligramo*10
    return jsonify({ "peso_mmi" : peso_mmi})    

@app.route("/miligramo-nanogramo/<string:miligramo>")
def get_datos_mn(miligramo):
    miligramo = float(miligramo)
    peso_mn = miligramo*100
    return jsonify({ "peso_mn" : peso_mn})    

@app.route("/microgramo-tonelada/<string:microgramo>")
def get_datos_miT(microgramo):
    microgramo = float(microgramo)
    peso_miT = microgramo/100000000
    return jsonify({ "peso_miT" : peso_miT})

@app.route("/microgramo-kilogramo/<string:microgramo>")
def get_datos_miK(microgramo):
    microgramo = float(microgramo)
    peso_miK = microgramo/10000000
    return jsonify({ "peso_miK" : peso_miK})   

@app.route("/microgramo-hectogramo/<string:microgramo>")
def get_datos_miH(microgramo):
    microgramo = float(microgramo)
    peso_miH = microgramo/1000000
    return jsonify({ "peso_miH" : peso_miH})   

@app.route("/microgramo-decagramo/<string:microgramo>")
def get_datos_miD(microgramo):
    microgramo = float(microgramo)
    peso_miD = microgramo/100000
    return jsonify({ "peso_miD" : peso_miD})   

@app.route("/microgramo-gramo/<string:microgramo>")
def get_datos_mig(microgramo):
    microgramo = float(microgramo)
    peso_mig = microgramo/10000
    return jsonify({ "peso_mig" : peso_mig})   

@app.route("/microgramo-decigramo/<string:microgramo>")
def get_datos_mid(microgramo):
    microgramo = float(microgramo)
    peso_mid = microgramo/1000
    return jsonify({ "peso_mid" : peso_mid})   

@app.route("/microgramo-centigramo/<string:microgramo>")
def get_datos_mic(microgramo):
    microgramo = float(microgramo)
    peso_mic = microgramo/100
    return jsonify({ "peso_mic" : peso_mic})   

@app.route("/microgramo-miligramo/<string:microgramo>")
def get_datos_mim(microgramo):
    microgramo = float(microgramo)
    peso_mim = microgramo/10
    return jsonify({ "peso_mim" : peso_mim})  

@app.route("/microgramo-microgramo/<string:microgramo>")
def get_datos_mimi(microgramo):
    peso_mimi = float(microgramo)
    return jsonify({ "peso_mimi" : peso_mimi})   

@app.route("/microgramo-nanogramo/<string:microgramo>")
def get_datos_min(microgramo):
    microgramo = float(microgramo)
    peso_min = microgramo*10
    return jsonify({ "peso_min" : peso_min})  

@app.route("/nanogramo-tonelada/<string:nanogramo>")
def get_datos_nT(nanogramo):
    nanogramo = float(nanogramo)
    peso_nT = nanogramo/1000000000
    return jsonify({ "peso_nT" : peso_nT})

@app.route("/nanogramo-kilogramo/<string:nanogramo>")
def get_datos_nK(nanogramo):
    nanogramo = float(nanogramo)
    peso_nK = nanogramo/100000000
    return jsonify({ "peso_nK" : peso_nK})

@app.route("/nanogramo-hectogramo/<string:nanogramo>")
def get_datos_nH(nanogramo):
    nanogramo = float(nanogramo)
    peso_nH = nanogramo/10000000
    return jsonify({ "peso_nH" : peso_nH})

@app.route("/nanogramo-decagramo/<string:nanogramo>")
def get_datos_nD(nanogramo):
    nanogramo = float(nanogramo)
    peso_nD = nanogramo/1000000
    return jsonify({ "peso_nD" : peso_nD})

@app.route("/nanogramo-gramo/<string:nanogramo>")
def get_datos_ng(nanogramo):
    nanogramo = float(nanogramo)
    peso_ng = nanogramo/100000
    return jsonify({ "peso_ng" : peso_ng})

@app.route("/nanogramo-decigramo/<string:nanogramo>")
def get_datos_nd(nanogramo):
    nanogramo = float(nanogramo)
    peso_nd = nanogramo/10000
    return jsonify({ "peso_nd" : peso_nd})

@app.route("/nanogramo-centigramo/<string:nanogramo>")
def get_datos_nc(nanogramo):
    nanogramo = float(nanogramo)
    peso_nc = nanogramo/1000
    return jsonify({ "peso_nc" : peso_nc})

@app.route("/nanogramo-miligramo/<string:nanogramo>")
def get_datos_nm(nanogramo):
    nanogramo = float(nanogramo)
    peso_nm = nanogramo/100
    return jsonify({ "peso_nm" : peso_nm})

@app.route("/nanogramo-microgramo/<string:nanogramo>")
def get_datos_nmi(nanogramo):
    nanogramo = float(nanogramo)
    peso_nmi = nanogramo/10
    return jsonify({ "peso_nmi" : peso_nmi})

@app.route("/nanogramo-nanogramo/<string:nanogramo>")
def get_datos_nn(nanogramo):
    peso_nn = float(nanogramo)
    return jsonify({ "peso_nn" : peso_nn})     

if __name__ == '_main_':
    app.run(debug=True, port=4000)
