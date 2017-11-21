import codecs
import ply.yacc as yacc
import compiler

# Parsing Rules

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)


def p_barnameh(p):
    """ barnameh  : PROGRAM_KW SHENASE tarifha """
    print('Rule #1      : barnameh -> PROGRAM_KW SHENASE tarifha')


def p_tarifha_1(p):
    """ tarifha  : tarifha tarif """
    print('Rule #2-1    : tarifha -> tarifha tarif')


def p_tarifha_2(p):
    """ tarifha  :  tarif """
    print('Rule #2-2    : tarifha -> tarif')


###
def p_tarif_1(p):
    """ tarif  : tarifeSakhtar """
    print('Rule #3-1    : tarif -> tarifeSakhtar')


def p_tarif_2(p):
    """ tarif : tarifeMoteghayyer """
    print('Rule #3-2    : tarif -> tarifeMoteghayyer')


def p_tarif_3(p):
    """ tarif : tarifeTabe """
    print('Rule #3-3    : tarif -> tarifeTabe')


###
def p_tarifeSakhtar(p):
    """ tarifeSakhtar : STRUCT_KW SHENASE OPEN_BRACE tarifhayeMahalli CLOSE_BRACE """
    print('Rule #4      : tarifeSakhtar -> STRUCT_KW SHENASE OPEN_BRACE tarifhayeMahalli CLOSE_BRACE ')


def p_tarifhayeMahalli_1(p):
    """ tarifhayeMahalli : tarifhayeMahalli tarifMoteghayyereMahdud """
    print('Rule #5-1     : tarifhayeMahalli -> tarifhayeMahalli tarifMoteghayyereMahdud')


def p_tarifhayeMahalli_2(p):
    """ tarifhayeMahalli : epsilon """
    print('Rule #5-2     : tarifhayeMahalli -> epsilon')


def p_tarifMoteghayyereMahdud(p):
    """ tarifMoteghayyereMahdud : jenseMahdud tarifhayeMoteghayyerha NOGHTE_VIRGUL """
    print('Rule #6      : tarifMoteghayyereMahdud -> jensMahdud tarifhayeMoteghayyerha NOGHTE_VIRGUL')


def p_jenseMahdud_1(p):
    """ jenseMahdud : CONST_KW jens """
    print('Rule #7-1     : jenseMahdud -> CONST_KW jens')


def p_jenseMahdud_2(p):
    """ jenseMahdud : jens """
    print('Rule #7-2     : jenseMahdud -> jens')


def p_jens_1(p):
    """ jens : INT_KW """
    print('Rule #8-1     : jens -> INT_KW')


def p_jens_2(p):
    """ jens : FLOAT_KW """
    print('Rule #8-2     : jens -> FLOAT_KW')


def p_jens_3(p):
    """ jens : BOOL_KW """
    print('Rule #8-3     : jens -> BOOL_KW')


def p_jens_4(p):
    """ jens : CHAR_KW """
    print('Rule #8-4     : jens -> CHAR_KW')


def p_tarifeMoteghayyer(p):
    """ tarifeMoteghayyer : jens tarifhayeMoteghayyerha NOGHTE_VIRGUL """
    print('Rule #9   : tarifeMoteghayyer -> jens tarifhayeMoteghayyerha ;')


def p_tarifhayeMoteghayyerha_1(p):
    """ tarifhayeMoteghayyerha : tarifeMeghdareAvvalie """
    print('Rule #10-1    : tarifhayeMoteghayyerha -> tarifeAvvalie')


def p_tarifhayeMoteghayyerha_2(p):
    """ tarifhayeMoteghayyerha : tarifhayeMoteghayyerha COMMA tarifeMeghdareAvvalie """
    print('Rule #10-2    : tarifhayeMoteghayyerha -> tarifhayeMoteghayyerha COMMA tarifeMeghdarAvvalie')


def p_tarifeMeghdareAvvalie_1(p):
    """ tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer """
    print('Rule #11-1    : tarifeMeghdarAvvalie -> tarifeShenaseyeMoteghayyer')


def p_tarifeMeghdareAvvalie_2(p):
    """ tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer EQUALS ebarateSade """
    print('Rule #11-2    : tarifeMeghdarAvvalie -> tarifeShenaseyeMoteghayyer EQUALS ebarateSade')


def p_tarifeShenaseyeMoteghayyer_1(p):
    """ tarifeShenaseyeMoteghayyer : SHENASE    """
    print('Rule #12-1    : tarifeShenaseyeMoteghayyer -> SHENASE')


def p_tarifeShenaseyeMoteghayyer_2(p):
    """ tarifeShenaseyeMoteghayyer : SHENASE OPEN_BRACKET INT CLOSE_BRACKET """
    print('Rule #12-2    : tarifeShenaseyeMoteghayyer -> SHENASE OPEN_BRACKET INT CLOSE_BRACKET ')


def p_tarifeShenaseyeMoteghayyer_3(p):
    """ tarifeShenaseyeMoteghayyer : SHENASE OPEN_BRACKET FLOAT CLOSE_BRACKET """
    print('Rule #12-3    : tarifeShenaseyeMoteghayyer -> SHENASE OPEN_BRACKET FLOAT CLOSE_BRACKET ')


def p_tarifeTabe_1(p):
    """ tarifeTabe : jens SHENASE   OPEN_PAREN  vorudi   CLOSE_PAREN  jomle """
    print('Rule #13-1    : tarifeTabe -> jens SHENASE   OPEN_PAREN  vorudi   CLOSE_PAREN  jomle')


def p_tarifeTabe_2(p):
    """ tarifeTabe : SHENASE   OPEN_PAREN  vorudi   CLOSE_PAREN  jomle """
    print('Rule #13-2    : tarifeTabe -> SHENASE   OPEN_PAREN  vorudi   CLOSE_PAREN  jomle')


def p_vorudi_1(p):
    """ vorudi : vorudiha """
    print('Rule #14-1    : vorudi -> vorudiha')


def p_vorudi_2(p):
    """ vorudi : epsilon """
    print('Rule #14-2    : vorudi -> epsilon ')


def p_vorudiha_1(p):
    """ vorudiha : vorudiha NOGHTE_VIRGUL jensVorudiha """
    print('Rule #15-1    : vorudiha -> vorudiha NOGHTE_VIRGUL jensVorudiha')


def p_vorudiha_2(p):
    """ vorudiha : jensVorudiha """
    print('Rule #15-2    : vorudiha -> jensVorudiha')


def p_jensVorudiha(p):
    """ jensVorudiha : jens shenaseyeVorudiha """
    print('Rule #16      : jensVorudiha -> jens shenaseyeVorudiha')


def p_shenaseyeVorudiha_1(p):
    """ shenaseyeVorudiha : shenaseyeVorudiha COMMA shenaseyeVorudi """
    print('Rule #17-1    : shenaseyeVorudiha -> shenaseyeVorudiha COMMA shenaseyeVorudi')


def p_shenaseyeVorudiha_2(p):
    """ shenaseyeVorudiha : shenaseyeVorudi """
    print('Rule #17-2    : shenaseyeVorudiha -> shenaseyeVorudi')


def p_shenaseyeVorudi_1(p):
    """ shenaseyeVorudi : SHENASE """
    print('Rule #18-1    : shenaseyeVorudi -> SHENASE')


def p_shenaseyeVorudi_2(p):
    """ shenaseyeVorudi : SHENASE OPEN_BRACKET CLOSE_BRACKET """
    print('Rule #18-2    : shenaseyeVorudi -> SHENASE OPEN_BRACKET CLOSE_BRACKET')


def p_jomle_1(p):
    """ jomle : jomleyeMorakkab """
    print('Rule #19-1    : jomle -> jomleyeMorakkab')


def p_jomle_2(p):
    """ jomle : jomleyeEbarat """
    print('Rule #19-2    : jomle -> jomleyeEbarat')


def p_jomle_3(p):
    """ jomle : jomleyeEntekhab """
    print('Rule #19-3    : jomle -> jomleyeEntekhab')


def p_jomle_4(p):
    """ jomle : jomleyeTekrar """
    print('Rule #19-4    : jomle -> jomleyeTekrar')


def p_jomle_5(p):
    """ jomle : jomleyeBazgasht """
    print('Rule #19-5    : jomle -> jomleyeBazgasht')


def p_jomle_6(p):
    """ jomle : jomleyeShekast """
    print('Rule #19-6    : jomle -> jomeleyeShekast')


def p_jomleyeMorakkab(p):
    """ jomleyeMorakkab : OPEN_BRACE tarifhayeMahalli jomleha CLOSE_BRACE """
    print('Rule #20      : jomleyeMorakkab -> OPEN_BRACE tarifhayeMahalli jomleha CLOSE_BRACE')


def p_jomleha_1(p):
    """ jomleha : jomleha jomle """
    print('Rule #21-1    : jomleha -> jomleha jomle')


def p_jomleha_2(p):
    """ jomleha : epsilon """
    print('Rule #21-1    : jomleha -> epsilon ')


def p_jomleyeEbarat_1(p):
    """ jomleyeEbarat : ebarat NOGHTE_VIRGUL """
    print('Rule #22-1    : jomleyeEbarat -> ebarat ;')


def p_jomleyeEbarat_2(p):
    """ jomleyeEbarat : NOGHTE_VIRGUL """
    print('Rule #22-2    : jomleyeEbarat -> ;')


def p_jomleyeEntekhab_1(p):
    """ jomleyeEntekhab : IF_KW ebarateSade THEN_KW jomle """
    print('Rule #23-1    : jomleyeEntekhab -> IF_KW ebarateSade THEN_KW jomle')


def p_jomleyeEntekhab_2(p):
    """ jomleyeEntekhab : IF_KW ebarateSade THEN_KW jomle ELSE_KW jomle """
    print('Rule #23-2    : jomleyeEntekhab -> IF_KW ebarateSade THEN_KW jomle ELSE_KW jomle')


def p_jomleyeEntekhab_3(p):
    """ jomleyeEntekhab : SWITCH_KW OPEN_PAREN  ebarateSade CLOSE_PAREN  onsoreHalat onsorePishfarz END_KW """
    print(
        'Rule #23-3    : jomleyeEntekhab -> SWITCH_KW OPEN_PAREN  ebarateSade CLOSE_PAREN  onsoreHalat onsorePishfarz END_KW')


def p_onsoreHalat_1(p):
    """ onsoreHalat : CASE_KW INT COLON jomle NOGHTE_VIRGUL """
    print('Rule #24-1    : onsoreHalat -> CASE_KW INT COLON jomle NOGHTE_VIRGUL')


def p_onsoreHalat_2(p):
    """ onsoreHalat : CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL """
    print('Rule #24-2    : onsoreHalat -> CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL')


def p_onsoreHalat_3(p):
    """ onsoreHalat : onsoreHalat CASE_KW INT COLON jomle NOGHTE_VIRGUL """
    print('Rule #24-3    : onsoreHalat -> onsoreHalat CASE_KW INT COLON jomle NOGHTE_VIRGUL')


def p_onsoreHalat_4(p):
    """ onsoreHalat : onsoreHalat CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL """
    print('Rule #24-4    : onsoreHalat -> onsoreHalat CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL')


def p_onsorePishfarz_1(p):
    """ onsorePishfarz : DEFAULT_KW COLON jomle NOGHTE_VIRGUL """
    print('Rule #25-1   : onsorePishfarz -> DEFAULT_KW COLON jomle NOGHTE_VIRGUL')


def p_onsorePishfarz_2(p):
    """ onsorePishfarz :  epsilon """
    print('Rule #25-2   : onsorePishfarz -> epsilon ')


def p_jomleyeTekrar(p):
    """ jomleyeTekrar : WHILE_KW OPEN_PAREN  ebarateSade   CLOSE_PAREN  jomle    """
    print('Rule #26     : jomleyeTekrar -> WHILE_KW OPEN_PAREN  ebarateSade   CLOSE_PAREN  jomle')


def p_jomleyeBazgasht_1(p):
    """jomleyeBazgasht :  RETURN_KW  NOGHTE_VIRGUL """
    print('Rule #28-1   : jomleyeBazgasht -> RETURN_KW  NOGHTE_VIRGUL')


def p_jomleyeBazgasht_2(p):
    """ jomleyeBazgasht : RETURN_KW ebarat NOGHTE_VIRGUL """
    print('Rule #28-2   : jomleyeBazgasht -> RETURN_KW ebarat NOGHTE_VIRGUL')


def p_jomleyeShekast(p):
    """ jomleyeShekast : BREAK_KW NOGHTE_VIRGUL """
    print('Rule #29     : jomleyeShekast -> BREAK_KW NOGHTE_VIRGUL')


def p_ebarat_1(p):
    """ ebarat : taghirpazir EQUALS ebarat """
    print('Rule #30-1   : ebarat -> taghirpazir EQUALS ebarat')


def p_ebarat_2(p):
    """ ebarat : taghirpazir PLUS_EQ ebarat """
    print('Rule #30-2   : ebarat -> taghirpazir PLUS_EQ ebarat')


def p_ebarat_3(p):
    """ ebarat : taghirpazir MINUS_EQ ebarat """
    print('Rule #30-3   : ebarat -> taghirpazir MINUS_EQ ebarat')


def p_ebarat_4(p):
    """ ebarat : taghirpazir TIMES_EQ ebarat """
    print('Rule #30-4   : ebarat -> taghirpazir TIMES_EQ ebarat')


def p_ebarat_5(p):
    """ ebarat : taghirpazir DIVIDE_EQ ebarat """
    print('Rule #30-5  : ebarat -> taghirpazir DIVIDE_EQ ebarat')


def p_ebarat_6(p):
    """ ebarat : taghirpazir PLUS_PLUS """
    print('Rule #30-6  : ebarat -> taghirpazir PLUS_PLUS')


def p_ebarat_7(p):
    """ebarat : taghirpazir MINUS_MINUS """
    print('Rule #30-7  : ebarat -> taghirpazir MINUS_MINUS')


def p_ebarat_8(p):
    """ ebarat : ebarateSade """
    print('Rule #30-8  : ebarat -> ebarateSade')


def p_ebarateSade_1(p):
    """ ebarateSade : ebarateSade OR_KW ebarateSade """
    print('Rule #31-1   : ebarateSade -> ebarateSade OR_KW ebarateSade')


def p_ebarateSade_2(p):
    """ ebarateSade : ebarateSade AND_KW ebarateSade """
    print('Rule #31-2   : ebarateSade -> ebarateSade AND_KW ebarateSade')


def p_ebarateSade_3(p):
    """ ebarateSade : ebarateSade SHORT_CIRCUIT_OR_KW ebarateSade """
    print('Rule #31-3   : ebarateSade -> ebarateSade SHORT_CIRCUIT_OR_KW ebarateSade')


def p_ebarateSade_4(p):
    """ ebarateSade : ebarateSade SHORT_CIRCUIT_AND_KW ebarateSade """
    print('Rule #31-4   : ebarateSade -> ebarateSade SHORT_CIRCUIT_AND_KW ebarateSade')


def p_ebarateSade_5(p):
    """ ebarateSade : NOT_KW ebarateSade """
    print('Rule #31-5   : ebarateSade -> NOT_KW ebarateSade')


def p_ebarateSade_6(p):
    """ ebarateSade : ebarateRabetei """
    print('Rule #31-6   : ebarateSade -> ebarateRabetei')


def p_ebarateRabetei_1(p):
    """ ebarateRabetei : ebarateRiaziManteghi """
    print('Rule #32-1   : ebarateRabetei -> ebarateRiaziManteghi')


def p_ebarateRabetei_2(p):
    """ ebarateRabetei : ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi """
    print('Rule #32-2   : ebarateRabetei -> ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi')


def p_amalgareRabetei_1(p):
    """ amalgareRabetei : LT  """
    print('Rule #33-1   : amalgareRabetei -> LT')


def p_amalgareRabetei_2(p):
    """ amalgareRabetei : GT  """
    print('Rule #33-2   : amalgareRabetei -> GT')


def p_amalgareRabetei_3(p):
    """ amalgareRabetei : GE """
    print('Rule #33-3   : amalgareRabetei -> GE')


def p_amalgareRabetei_4(p):
    """ amalgareRabetei : LE """
    print('Rule #33-4   : amalgareRabetei -> LE')


def p_amalgareRabetei_5(p):
    """ amalgareRabetei : EQ """
    print('Rule #33-5   : amalgareRabetei -> EQ')


def p_ebarateRiaziManteghi_1(p):
    """ ebarateRiaziManteghi : ebarateYegani """
    print('Rule #34-1   : ebarateRiaziManteghi -> ebarateYegani')


def p_ebarateRiaziManteghi_2(p):
    """ebarateRiaziManteghi : ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi """
    print('Rule #34-2   : ebarateRiaziManteghi -> ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi')


def p_amalgareRiazi_1(p):
    """ amalgareRiazi : PLUS """
    print('Rule #35-1   : amalgareRiazi -> PLUS')


def p_amalgareRiazi_2(p):
    """ amalgareRiazi : MINUS """
    print('Rule #35-2   : amalgareRiazi -> MINUS')


def p_amalgareRiazi_3(p):
    """ amalgareRiazi : TIMES """
    print('Rule #35-3   : amalgareRiazi -> TIMES')


def p_amalgareRiazi_4(p):
    """ amalgareRiazi : DIVIDE """
    print('Rule #35-4   : amalgareRiazi -> DIVIDE')


def p_amalgareRiazi_5(p):
    """ amalgareRiazi : MOD """
    print('Rule #35-5   : amalgareRiazi -> MOD')


def p_ebarateYegani_1(p):
    """ ebarateYegani : amalgareYegani ebarateYegani """
    print('Rule #36-1   : ebarateYegani -> amalgareYegani ebarateYegani')


def p_ebarateYegani_2(p):
    """ ebarateYegani : amel """
    print('Rule #36-2   : ebarateYegani -> amel')


def p_amalgareYegani_1(p):
    """ amalgareYegani : MINUS """
    print('Rule #37-1   : amalgareYegani -> MINUS')


def p_amalgareYegani_2(p):
    """ amalgareYegani : TIMES """
    print('Rule #37-2   : amalgareYegani -> TIMES')


def p_amalgareYegani_3(p):
    """ amalgareYegani : QUESTION_MARK """
    print('Rule #37-3   : amalgareYegani -> QUESTION_MARK')


def p_amel_1(p):
    """ amel : taghirpazir """
    print('Rule #38-1   : amel -> taghirpazir')


def p_amel_2(p):
    """ amel :  taghirnapazir """
    print('Rule #38-2   : amel -> taghirnapazir')


def p_taghirpazir_1(p):
    """ taghirpazir : SHENASE """
    print('Rule #39-1   : taghirpazir -> SHENASE')


def p_taghirpazir_2(p):
    """ taghirpazir : taghirpazir OPEN_BRACKET ebarat CLOSE_BRACKET """
    print('Rule #39-2   : taghirpazir -> taghirpazir OPEN_BRACKET ebarat CLOSE_BRACKET')


def p_taghirpazir_3(p):
    """taghirpazir : taghirpazir DOT SHENASE """
    print('Rule #39-3   : taghirpazir -> taghirpazir DOT SHENASE')


def p_taghirnapazir_1(p):
    """ taghirnapazir : OPEN_PAREN ebarat CLOSE_PAREN """
    print('Rule #40-1   : taghirnapazir -> OPEN_PAREN ebarat CLOSE_PAREN')


def p_taghirnapazir_2(p):
    """ taghirnapazir : sedaZadan """
    print('Rule #40-2   : taghirnapazir -> sedaZadan')


def p_taghirnapazir_3(p):
    """taghirnapazir : meghdareSabet """
    print('Rule #40-3   : taghirnapazir -> meghdarSabet')


def p_sedaZadan(p):
    """ sedaZadan : SHENASE OPEN_PAREN bordareVorudi CLOSE_PAREN """
    print('Rule #40     : sedaZadan -> SHENASE OPEN_PAREN bordareVorudi CLOSE_PAREN ')


def p_bordareVorudi_1(p):
    """ bordareVorudi : bordareVorudiha """
    print('Rule #41-1   : bordareVorudi -> bordareVorudiha')


def p_bordareVorudi_2(p):
    """ bordareVorudi : epsilon """
    print('Rule #41-2   : bordareVorudi -> epsilon ')


def p_bordareVorudiha_1(p):
    """ bordareVorudiha : bordareVorudiha COMMA ebarat """
    print('Rule #42-1   : bordareVorudiha -> bordareVorudiha COMMA ebarat')


def p_bordareVorudiha_2(p):
    """bordareVorudiha : ebarat """
    print('Rule #42-2 : bordareVorudiha -> ebarat')


def p_meghdareSabet_1(p):
    """ meghdareSabet : INT """
    print('Rule #43-1 : meghdareSabet -> INT ')


def p_meghdareSabet_2(p):
    """ meghdareSabet :  FLOAT """
    print('Rule #43-2 : meghdareSabet -> FLOAT ')


def p_meghdareSabet_3(p):
    """ meghdareSabet :  HARFE_SABET """
    print('Rule #43-3 : meghdareSabet -> HARFE_SABET ')


def p_meghdareSabet_4(p):
    """ meghdareSabet : TRUE_KW """
    print('Rule #43-4 : meghdareSabet -> TRUE_KW ')


def p_meghdareSabet_5(p):
    """ meghdareSabet : FALSE_KW """
    print('Rule #43-5 : meghdareSabet -> FALSE_KW ')


def p_epsilon(p):
    """epsilon : """
    pass


def p_error(p):
    if p:
        print('Syntax Error')
    else:
        print('Syntax Error EOF')


tokens = compiler.tokens

parser = yacc.yacc()
f = codecs.open('./sample.txt', encoding='utf-8')
r = ''
for i in f:
    r += str(i)
result = parser.parse(r, lexer=compiler.lexical_analyser)
f.close()
print(result)
