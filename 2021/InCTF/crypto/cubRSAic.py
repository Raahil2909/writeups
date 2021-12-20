#!/usr/bin/python3
a=1
b=193397088739638251960555612436875600986330023883750295571725584630414480365724395898270141722031329748156082442012506741700345490623652456944752641259299481648189663225789316735492124809430246787061623943122992972555612870003055978190998434876318194750716018238436902415663573233192086436098541111277008199813
c=8728831297832120843336404142494383487861941996882802023565995709954417891405655853020017387748976733140991007940950795977416209344692420808833741595065361790155014723446976903204381140455085622575477064605600925830092628718070785954578133863918237568921639276619726474929358824725452522548936820930316044199781907769975116642583087228056122086340804371487673925003430886366328940606581590239833871087344153426940165114190628567985514860529931412375128745713119805742019339702063634799522188535333496263711303227429950221230519245843532481700865129308471919982350847692475752700865209968245261953392636533410992980775
d=63070596256679484662413410207373928004736001790383956853307898306602698350449502470396308261161065806877977215076829311908943777778986616540253214462303167277670756699548339028092316959537033018041441628359647493347189674598031375658196799172454802634799166223829305392192521613748720703056322649928224065867121497675495400662468690132676998903424015988906876418063546949676385421158504886275413258353832927820154529362504173957845256741347439175151413191454309190779489182687927387632163531223048994443162863182633645603482086186470861356033199650558396270818562930850023584234133180617891209746554867462265585965013354965873061584035287994018488964953755160036085993213998304861556792215861795195160484204162254562357064980532222046820367893936950321067965117665776931
e=0x10001

x = [121634004770817487027576901349955844506576645181037911605988943356350767883627569847166326486397613048031611450896209895194445039739571040618185274004390530382037821239076620033302875262875950534876288239157863266019935778326440224340173730802867411876318977528784758029431662385342841157436296620207562218729, 71763083968820764932978711086919756479753378702712383965736641274063712482096826051103815235633716700124470991116296846505900450884081416326567367254908944040603070945210125950186713526004901886251806976746820356373574378255778099843763267882833736855628148799328424573171569635978727017610845101305594299027, 7225548771041502570752002536020549394365933528727218309350162102713420837654007061436190617046018768891910323719813060341211870518261051399389763851682057]

# p = sqrt(x[0])
pqr = [11028780747245702999399582287572422141860235227169584753700396836978683591866678949333185731496840507050073213352286079907426425697620387818057555212467027, 9931852409111441803548946889619359095211948865688705654282179803242049937272278415968476455693954007505687204320789626803285531310303921968435241366305211, x[2]]

n = 0x540fa632c6fb3c9d26d1927addf3775f15c44651636068ca9e7ba57cc5c0eecfae7fccb7174ad9594fee114551ded48029203c2cf2775f48e755b9275cf5be199dcfbe110ff480166ce902726c08560f9e05a0c823d5603c34c10e2b1df09d5121c804fb980d718d45c508d1a760f7c6068f19d53787deb1c9b89c3b64e5360498bed3d5be6d30aa1964d09a6ba179064345cfadce5916f32ec295653e8fc7c1fb9f225253566c9a8c168800e58d5141eff1c2be8e9f47b4a083992c39ceb6a9

ct = 0xa17638f7fb80df8e96d78fddb3324d26395aaf30aa49610db4ed4bf3ef9864a32f32a7e11468440540abef648754a11e98fd836f077ac6d9bc33d6df0190fe62e900b02e62a95268b76ae2d673b3c614a82c267f213219ebd9ba8313fc078a541eeff0fcc1dfec568539098682c824d0bdd78933f2421d52d57aaf2c82bcaff304d3d3dd251c289d2fc93292c5c9734871cf491b355ce20277558902484fd9dc85de87caccbb5474b14b9664037f213344d9d77a1e10fb8f1d6f42f11e9247b

phi = (pqr[0]-1)*(pqr[1]-1)*(pqr[2]-1)
key = pow(e,-1,phi)
pt = pow(ct,key,n)
print(bytes.fromhex(hex(pt)[2:]).decode())
