f = open("arquivo.csv", "r") 

#contador pathology
p_ben = 0 
p_call = 0
p_mal = 0


#contador de linhas
max_l =-1

#contator do breast_density
bes_d_1 = 0
bes_d_2 =0
bes_d_3 =0
bes_d_4 =0

#contador do mass shaphe
ar_di = 0
iar_di = 0
ab_t = 0
fa_d=0
ir_r = 0
irr_f =0
lo_b = 0
lo_ad =0
lo_ir = 0
lol_n = 0
lo_ov = 0
ly_no= 0
n_a = 0
ov_a = 0
ol_nd =0
r_o = 0
ri_ad=0
ro_l= 0
ro_ov = 0
#contador mass margins:
	
	
# diminuir  os nomes de Variaveis

#pathology
BWC = "BENIGN_WITHOUT_CALLBACK"

#mass sharphe
ARC_D="ARCHITECTURAL_DISTORTION"
IARC_D = "IRREGULAR-ARCHITECTURAL_DISTORTION"
ABT = "ASYMMETRIC_BREAST_TISSUE"
FAD = "FOCAL_ASYMMETRIC_DENSITY"
IRR_F_D = "IRREGULAR-FOCAL_ASYMMETRIC_DENSITY"
LO_A_D="LOBULATED-ARCHITECTURAL_DISTORTION"
LO_I="LOBULATED-IRREGULAR"
LO_L_N="LOBULATED-LYMPH_NODE"
LO_O="LOBULATED-OVAL"
LY_N="LYMPH_NODE"
OL_N="OVAL-LYMPH_NODE"
RIA_D="ROUND-IRREGULAR-ARCHITECTURAL_DISTORTION"
RL="ROUND-LOBULATED"
RO_O="ROUND-OVAL"
#mass margins:

linhas = f.readlines() 
 
for linha in linhas:
	lista=linha.split(',')
	max_l+=1        # contado de linhas
	
	#Testo do breast_density
	if "1"  in lista[1]:
		bes_d_1+=1
		
	if "2" in lista[1]:
		bes_d_2+=1
	
	if "3" in lista[1]:
		bes_d_3+=1

	if "4" in lista[1]:
		bes_d_4+=1
	
	#Testador do mass sharphe
	elif ABT == lista[6]:
		ab_t+=1
	
	if FAD == lista[6]:
		fa_d +=1
	
	if IRR_F_D == lista[6]:
		irr_f+=1
	
	if IARC_D == lista[6]:
		iar_di +=1
	
	elif ARC_D == lista[6]:
		ar_di +=1
	
	elif "IRREGULAR" == lista[6]:
		ir_r +=1
	#elif LO_A_D in linha:
		#lo_ad +=1
		
	elif "LOBULATED" == lista[6]:
		lo_b +=1
	
	if LO_A_D == lista[6]:
		lo_ad+=1
	
	if LO_I == lista[6]:
		lo_ir+=1
	
	if LO_L_N == lista[6]:
		lol_n+=1
		
	if LO_O == lista[6]:
		lo_ov+=1
	
	if LY_N == lista[6]:
		ly_no+=1
	
	if "N/A" == lista[6]:
		n_a+=1
	
	if "OVAL" == lista[6]:
		ov_a+=1
	
	if OL_N == lista[6]:
		ol_nd+=1
	
	if "ROUND" == lista[6]:
		r_o+=1
		
	if RIA_D  == lista[6]:
		ri_ad+=1
	if RL == lista[6]:
		ro_l+=1
	if RO_O == lista[6]:
		ro_ov+=1
		

	
	#Testador do pathology
	if BWC == lista[9]:
		p_call +=1
	
	elif "BENIGN" == lista[9]:
		p_ben+=1
	
	elif "MALIGNANT" == lista[9]:
		p_mal+=1

#porcentagem de pathology
E = p_call / max_l * 100
B = p_ben / max_l * 100
M = p_mal / max_l * 100

#porcentagem de breast_density
BD_1 = bes_d_1 / max_l * 100
BD_2 = bes_d_2 / max_l * 100
BD_3 = bes_d_3 / max_l * 100
BD_4 = bes_d_4 / max_l * 100

#porcentagem de mass shape
AR_DP = ar_di / max_l * 100
IAR_DP = iar_di / max_l * 100
ABT_P = ab_t  / max_l * 100
FAD_P = fa_d /max_l * 100
IRRE_P = ir_r / max_l *100
IRRE_F_D = irr_f / max_l *100
LOB_P= lo_b / max_l *100
LOAD_P= lo_ad / max_l *100
LOIR_P = lo_ir / max_l * 100
LOLN_P = lol_n / max_l * 100
LOOV_P = lo_ov / max_l *100
LYN_P = ly_no / max_l *100
NA_P = n_a / max_l *100
OVA_P = ov_a / max_l *100
OLN_P = ol_nd / max_l *100
RO_P = r_o / max_l * 100
RIAD_P = ri_ad / max_l * 100
RL_P = ro_l / max_l * 100
RO_OV = ro_ov / max_l *100
arquivo = open('Relatorio.txt', 'w')

#porcentagem em mass margins:
	

arquivo.write("breast_density:\n")

arquivo.write(f"1: {bes_d_1}: ({BD_1:.2f} %)\n")
arquivo.write(f"2: {bes_d_2}: ({BD_2:.2f} %)\n")
arquivo.write(f"3: {bes_d_3}: ({BD_3:.2f} %)\n")
arquivo.write(f"4: {bes_d_4}: ({BD_4:.2f} %)\n\n")

arquivo.write("mass shape:\n")
arquivo.write(f"ARCHITECTURAL_DISTORTION:{ar_di} :({AR_DP:.2f}%)\n")
arquivo.write(f"ASYMMETRIC_BREAST_TISSUE :{ab_t} :({ABT_P:.2f}%)\n")
arquivo.write(f"FOCAL_ASYMMETRIC_DENSITY :{fa_d} :({FAD_P:.2f}%)\n")
arquivo.write(f"IRREGULAR :{ir_r} :({IRRE_P:.2f}%)\n")
arquivo.write(f"IRREGULAR-ARCHITECTURAL_DISTORTION:{iar_di} :({IAR_DP:.2f}%)\n")
arquivo.write(f"IRREGULAR-FOCAL_ASYMMETRIC_DENSITY:{irr_f} :({IRRE_F_D:.2f}%)\n")
arquivo.write(f"LOBULATED:{lo_b} :({LOB_P:.2f}%)\n")
arquivo.write(f"LOBULATED-ARCHITECTURAL_DISTORTION:{lo_ad} :({LOAD_P:.2f}%)\n")

arquivo.write(f"LOBULATED-IRREGULAR: {lo_ir} :({LOIR_P:.2f}%)\n")
arquivo.write(f"LOBULATED-LYMPH_NODE: {lol_n} :({LOLN_P:.2f}%)\n")
arquivo.write(f"LOBULATED-OVAL: {lo_ov} :({LOOV_P:.2f}%)\n")
arquivo.write(f"LYMPH_NODE: {ly_no} :({LYN_P:.2f}%)\n")
arquivo.write(f"N/A: {n_a} :({NA_P:.2f}%)\n")
arquivo.write(f"OVAL: {ov_a} :({OVA_P:.2f}%)\n")
arquivo.write(f"OVAL-LYMPH_NODE: {ol_nd} :({OLN_P:.2f}%)\n")
arquivo.write(f"ROUND: {r_o} :({RO_P:.2f}%)\n")
arquivo.write(f"ROUND-IRREGULAR-ARCHITECTURAL_DISTORTION: {ri_ad} :({RIAD_P:.2f}%)\n")
arquivo.write(f"ROUND-LOBULATED: {ro_l} :({RL_P:.2f}%)\n")
arquivo.write(f"ROUND-OVAL: {ro_ov} :({RO_OV:.2f}%)\n\n")


#AQUI
arquivo.write("pathology:\n")
arquivo.write("BENIGN: %d (%.2f%%)\n" %(p_ben, B))
arquivo.write("ENIGN_WITHOUT_CALLBACK: %d (%.2f%%)\n" %(p_call,  E))
arquivo.write("MALIGNANT: %d (%.2f%%)\n"%(p_mal, M))

f.close()

print("breast_density")
print(f"{bes_d_1}: ({BD_1:.2f} %)")
print(f"{bes_d_2}: ({BD_2:.2f} %)")
print(f"{bes_d_3}: ({BD_3:.2f} %)")
print(f"{bes_d_4}: ({BD_4:.2f} %)\n")

print("mass shape")
print(f"ARCHITECTURAL_DISTORTION:{ar_di} :({AR_DP:.2f}%)")
print(f"ASYMMETRIC_BREAST_TISSUE :{ab_t} :({ABT_P:.2f}%)")
print(f"FOCAL_ASYMMETRIC_DENSITY :{fa_d} :({FAD_P:.2f}%)")
print(f"IRREGULAR :{ir_r} :({IRRE_P:.2f}%)")
print(f"IRREGULAR-ARCHITECTURAL_DISTORTION:{iar_di} :({IAR_DP:.2f}%)")
print(f"IRREGULAR-FOCAL_ASYMMETRIC_DENSITY:{irr_f} :({IRRE_F_D:.2f}%)")
print(f"LOBULATED:{lo_b} :({LOB_P:.2f}%)")
print(f"LOBULATED-ARCHITECTURAL_DISTORTION:{lo_ad} :({LOAD_P:.2f}%)")

print(f"LOBULATED-IRREGULAR: {lo_ir} :({LOIR_P:.2f}%)")
print(f"LOBULATED-LYMPH_NODE: {lol_n} :({LOLN_P:.2f}%)")
print(f"LOBULATED-OVAL: {lo_ov} :({LOOV_P:.2f}%)")
print(f"LYMPH_NODE: {ly_no} :({LYN_P:.2f}%)")
print(f"N/A: {n_a} :({NA_P:.2f}%)")
print(f"OVAL: {ov_a} :({OVA_P:.2f}%)")
print(f"OVAL-LYMPH_NODE: {ol_nd} :({OLN_P:.2f}%)")
print(f"ROUND: {r_o} :({RO_P:.2f}%)")
print(f"ROUND-IRREGULAR-ARCHITECTURAL_DISTORTION: {ri_ad} :({RIAD_P:.2f}%)")
print(f"ROUND-LOBULATED: {ro_l} :({RL_P:.2f}%)")
print(f"ROUND-OVAL: {ro_ov} :({RO_OV:.2f}%)\n")


print("\033[1mpathology: ")

print("\033[34;1mBENIGN: %d (%.2f%%)\033[m" %(p_ben, B))

print("\033[33;1mENIGN_WITHOUT_CALLBACK: %d (%.2f%%)\033[m" %(p_call, E))

print("\033[31;1mMALIGNANT: %d (%.2f%%)\033[m" %(p_mal, M))
