import ply.yacc as yacc
import lex
from var import Var
from quad_ruple import QuadRuple
from op import Operator

qr = QuadRuple()
var = lex.variables
code = ''

precedence = (
    ('left', 'OR_KW', 'SHORT_CIRCUIT_OR_KW'),
    ('left', 'AND_KW', 'SHORT_CIRCUIT_AND_KW'),
    ('left', 'EQ'),
    ('left', 'LT', 'GT', 'LE', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MOD'),
    ('left', 'TIMES', 'DIVIDE'),
    # ('left', 'INT_KW', 'FLOAT_KW', 'CHAR_KW'),
    ('right', 'NOT_KW', 'MINUS_MINUS', 'PLUS_PLUS'),
)


def p_barnameh(p):
    """ barnameh : PROGRAM_KW SHENASE tarifha """
    # print('Rule #1 \t: barnameh -> PROGRAM_KW SHENASE tarifha')
    var[p[2]].type = 'Program'


def p_tarifha_1(p):
    """ tarifha : tarifha tarif """
    # print('Rule #2-1 \t: tarifha -> tarifha tarif')


def p_tarifha_2(p):
    """ tarifha : tarif """
    # print('Rule #2-2 \t: tarifha -> tarif')


def p_tarif_1(p):
    """ tarif : tarifeSakhtar """
    # print('Rule #3-1 \t: tarif -> tarifeSakhtar')


def p_tarif_2(p):
    """ tarif : tarifeMoteghayyer """
    # print('Rule #3-2 \t: tarif -> tarifeMoteghayyer')


def p_tarif_3(p):
    """ tarif : tarifeTabe """
    # print('Rule #3-3 \t: tarif -> tarifeTabe')


def p_tarifeSakhtar(p):
    """ tarifeSakhtar : STRUCT_KW SHENASE OPEN_BRACE tarifhayeMahalli CLOSE_BRACE """
    # print('Rule #4 \t: tarifeSakhtar -> STRUCT_KW SHENASE OPEN_BRACE tarifhayeMahalli CLOSE_BRACE ')


def p_tarifhayeMahalli_1(p):
    """ tarifhayeMahalli : tarifhayeMahalli tarifMoteghayyereMahdud """
    # print('Rule #5-1 \t: tarifhayeMahalli -> tarifhayeMahalli tarifMoteghayyereMahdud')


def p_tarifhayeMahalli_2(p):
    """ tarifhayeMahalli : epsilon """
    # print('Rule #5-2 \t: tarifhayeMahalli -> epsilon')


def p_tarifMoteghayyereMahdud(p):
    """ tarifMoteghayyereMahdud : jenseMahdud tarifhayeMoteghayyerha NOGHTE_VIRGUL """
    # print('Rule #6 \t: tarifMoteghayyereMahdud -> jensMahdud tarifhayeMoteghayyerha NOGHTE_VIRGUL')
    for v in p[2]:
        if v.type is None or v.type == p[1].type:
            v.type = p[1].type
            var[v.place].type = v.type
            var[v.place].value = v.value
            # print(str(var[v.place]))
        else:
            raise Exception('type mismatch error near ' + v.place + ' = ' + str(v.value))


def p_jenseMahdud_1(p):
    """ jenseMahdud : CONST_KW jens """
    # print('Rule #7-1 \t: jenseMahdud -> CONST_KW jens')
    p[0] = p[1]
    p[0].is_const = True


def p_jenseMahdud_2(p):
    """ jenseMahdud : jens """
    # print('Rule #7-2 \t: jenseMahdud -> jens')
    p[0] = p[1]


def p_jens_1(p):
    """ jens : INT_KW """
    # print('Rule #8-1 \t: jens -> INT_KW')
    p[0] = Var(type='int')


def p_jens_2(p):
    """ jens : FLOAT_KW """
    # print('Rule #8-2 \t: jens -> FLOAT_KW')
    p[0] = Var(type='float')


def p_jens_3(p):
    """ jens : BOOL_KW """
    # print('Rule #8-3 \t: jens -> BOOL_KW')
    p[0] = Var(type='bool')


def p_jens_4(p):
    """ jens : CHAR_KW """
    # print('Rule #8-4 \t: jens -> CHAR_KW')
    p[0] = Var(type='char')


def p_tarifeMoteghayyer(p):
    """ tarifeMoteghayyer : jens tarifhayeMoteghayyerha NOGHTE_VIRGUL """
    print('Rule #9 \t: tarifeMoteghayyer -> jens tarifhayeMoteghayyerha NOGHTE_VIRGUL')
    for v in p[2]:
        if v.type is None or v.type == p[1].type:
            v.type = p[1].type
        else:
            raise Exception('type mismatch error near ' + v.place + ' = ' + str(v.value))


def p_tarifhayeMoteghayyerha_1(p):
    """ tarifhayeMoteghayyerha : tarifeMeghdareAvvalie """
    # print('Rule #10-1 \t: tarifhayeMoteghayyerha -> tarifeMeghdareAvvalie')
    p[0] = p[1]


def p_tarifhayeMoteghayyerha_2(p):
    """ tarifhayeMoteghayyerha : tarifhayeMoteghayyerha COMMA tarifeMeghdareAvvalie """
    # print('Rule #10-2 \t: tarifhayeMoteghayyerha -> tarifhayeMoteghayyerha COMMA tarifeMeghdarAvvalie')
    p[1].append(p[3])
    p[0] = p[1]


def p_tarifeMeghdareAvvalie_1(p):
    """ tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer """
    # print('Rule #11-1 \t: tarifeMeghdarAvvalie -> tarifeShenaseyeMoteghayyer')
    p[0] = [p[1]]


def p_tarifeMeghdareAvvalie_2(p):
    """ tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer EQUALS ebarateSade """
    # print('Rule #11-2 \t: tarifeMeghdarAvvalie -> tarifeShenaseyeMoteghayyer EQUALS ebarateSade')
    p[1].value, p[1].type = p[3].value, p[3].type
    p[0] = p[1]


def p_tarifeShenaseyeMoteghayyer_1(p):
    """ tarifeShenaseyeMoteghayyer : SHENASE """
    # print('Rule #12-1 \t: tarifeShenaseyeMoteghayyer -> SHENASE')
    p[0] = Var(place=p[1])


def p_tarifeShenaseyeMoteghayyer_2(p):
    """ tarifeShenaseyeMoteghayyer : SHENASE OPEN_BRACKET INT CLOSE_BRACKET """
    # print('Rule #12-2 \t: tarifeShenaseyeMoteghayyer -> SHENASE OPEN_BRACKET INT CLOSE_BRACKET ')


# def p_tarifeShenaseyeMoteghayyer_3(p):
#     """ tarifeShenaseyeMoteghayyer : SHENASE OPEN_BRACKET FLOAT CLOSE_BRACKET """
#     # print('Rule #12-3 \t: tarifeShenaseyeMoteghayyer -> SHENASE OPEN_BRACKET FLOAT CLOSE_BRACKET ')


def p_tarifeTabe_1(p):
    """ tarifeTabe : jens SHENASE OPEN_PAREN vorudi CLOSE_PAREN jomle """
    # print('Rule #13-1 \t: tarifeTabe -> jens SHENASE OPEN_PAREN  vorudi   CLOSE_PAREN  jomle')


def p_tarifeTabe_2(p):
    """ tarifeTabe : SHENASE OPEN_PAREN vorudi CLOSE_PAREN jomle """
    # print('Rule #13-2 \t: tarifeTabe -> SHENASE   OPEN_PAREN  vorudi   CLOSE_PAREN  jomle')


def p_vorudi_1(p):
    """ vorudi : vorudiha """
    # print('Rule #14-1 \t: vorudi -> vorudiha')


def p_vorudi_2(p):
    """ vorudi : epsilon """
    # print('Rule #14-2 \t: vorudi -> epsilon ')


def p_vorudiha_1(p):
    """ vorudiha : vorudiha NOGHTE_VIRGUL jensVorudiha """
    # print('Rule #15-1 \t: vorudiha -> vorudiha NOGHTE_VIRGUL jensVorudiha')


def p_vorudiha_2(p):
    """ vorudiha : jensVorudiha """
    # print('Rule #15-2 \t: vorudiha -> jensVorudiha')


def p_jensVorudiha(p):
    """ jensVorudiha : jens shenaseyeVorudiha """
    # print('Rule #16 \t: jensVorudiha -> jens shenaseyeVorudiha')


def p_shenaseyeVorudiha_1(p):
    """ shenaseyeVorudiha : shenaseyeVorudiha COMMA shenaseyeVorudi """
    # print('Rule #17-1 \t: shenaseyeVorudiha -> shenaseyeVorudiha COMMA shenaseyeVorudi')


def p_shenaseyeVorudiha_2(p):
    """ shenaseyeVorudiha : shenaseyeVorudi """
    # print('Rule #17-2 \t: shenaseyeVorudiha -> shenaseyeVorudi')


def p_shenaseyeVorudi_1(p):
    """ shenaseyeVorudi : SHENASE """
    # print('Rule #18-1 \t: shenaseyeVorudi -> SHENASE')


def p_shenaseyeVorudi_2(p):
    """ shenaseyeVorudi : SHENASE OPEN_BRACKET CLOSE_BRACKET """
    # print('Rule #18-2 \t: shenaseyeVorudi -> SHENASE OPEN_BRACKET CLOSE_BRACKET')


def p_jomle_1(p):
    """ jomle : jomleyeMorakkab """
    # print('Rule #19-1 \t: jomle -> jomleyeMorakkab')


def p_jomle_2(p):
    """ jomle : jomleyeEbarat """
    # print('Rule #19-2 \t: jomle -> jomleyeEbarat')


def p_jomle_3(p):
    """ jomle : jomleyeEntekhab """
    # print('Rule #19-3 \t: jomle -> jomleyeEntekhab')


def p_jomle_4(p):
    """ jomle : jomleyeTekrar """
    # print('Rule #19-4 \t: jomle -> jomleyeTekrar')


def p_jomle_5(p):
    """ jomle : jomleyeBazgasht """
    # print('Rule #19-5 \t: jomle -> jomleyeBazgasht')


def p_jomle_6(p):
    """ jomle : jomleyeShekast """
    # print('Rule #19-6 \t: jomle -> jomeleyeShekast')


def p_jomleyeMorakkab(p):
    """ jomleyeMorakkab : OPEN_BRACE tarifhayeMahalli jomleha CLOSE_BRACE """
    # print('Rule #20 \t: jomleyeMorakkab -> OPEN_BRACE tarifhayeMahalli jomleha CLOSE_BRACE')


def p_jomleha_1(p):
    """ jomleha : jomleha jomle """
    # print('Rule #21-1 \t: jomleha -> jomleha jomle')


def p_jomleha_2(p):
    """ jomleha : epsilon """
    # print('Rule #21-1 \t: jomleha -> epsilon ')


def p_jomleyeEbarat_1(p):
    """ jomleyeEbarat : ebarat NOGHTE_VIRGUL """
    # print('Rule #22-1 \t: jomleyeEbarat -> ebarat ;')


def p_jomleyeEbarat_2(p):
    """ jomleyeEbarat : NOGHTE_VIRGUL """
    # print('Rule #22-2 \t: jomleyeEbarat -> ;')


def p_jomleyeEntekhab_1(p):
    """ jomleyeEntekhab : IF_KW ebarateSade THEN_KW jomle """
    # print('Rule #23-1 \t: jomleyeEntekhab -> IF_KW ebarateSade THEN_KW jomle')


def p_jomleyeEntekhab_2(p):
    """ jomleyeEntekhab : IF_KW ebarateSade THEN_KW jomle ELSE_KW jomle """
    # print('Rule #23-2 \t: jomleyeEntekhab -> IF_KW ebarateSade THEN_KW jomle ELSE_KW jomle')


def p_jomleyeEntekhab_3(p):
    """ jomleyeEntekhab : SWITCH_KW OPEN_PAREN  ebarateSade CLOSE_PAREN  onsoreHalat onsorePishfarz END_KW """
    # print('Rule #23-3 \t: jomleyeEntekhab -> SWITCH_KW OPEN_PAREN  ebarateSade CLOSE_PAREN  onsoreHalat '
    #       'onsorePishfarz END_KW')


def p_onsoreHalat_1(p):
    """ onsoreHalat : CASE_KW INT COLON jomle NOGHTE_VIRGUL """
    # print('Rule #24-1 \t: onsoreHalat -> CASE_KW INT COLON jomle NOGHTE_VIRGUL')


def p_onsoreHalat_2(p):
    """ onsoreHalat : CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL """
    # print('Rule #24-2 \t: onsoreHalat -> CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL')


def p_onsoreHalat_3(p):
    """ onsoreHalat : onsoreHalat CASE_KW INT COLON jomle NOGHTE_VIRGUL """
    # print('Rule #24-3 \t: onsoreHalat -> onsoreHalat CASE_KW INT COLON jomle NOGHTE_VIRGUL')


def p_onsoreHalat_4(p):
    """ onsoreHalat : onsoreHalat CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL """
    # print('Rule #24-4 \t: onsoreHalat -> onsoreHalat CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL')


def p_onsorePishfarz_1(p):
    """ onsorePishfarz : DEFAULT_KW COLON jomle NOGHTE_VIRGUL """
    # print('Rule #25-1 \t: onsorePishfarz -> DEFAULT_KW COLON jomle NOGHTE_VIRGUL')


def p_onsorePishfarz_2(p):
    """ onsorePishfarz :  epsilon """
    # print('Rule #25-2 \t: onsorePishfarz -> epsilon ')


def p_jomleyeTekrar(p):
    """ jomleyeTekrar : WHILE_KW OPEN_PAREN  ebarateSade   CLOSE_PAREN  jomle    """
    # print('Rule #26 \t: jomleyeTekrar -> WHILE_KW OPEN_PAREN  ebarateSade   CLOSE_PAREN  jomle')


def p_jomleyeBazgasht_1(p):
    """jomleyeBazgasht :  RETURN_KW  NOGHTE_VIRGUL """
    # print('Rule #28-1 \t: jomleyeBazgasht -> RETURN_KW  NOGHTE_VIRGUL')


def p_jomleyeBazgasht_2(p):
    """ jomleyeBazgasht : RETURN_KW ebarat NOGHTE_VIRGUL """
    # print('Rule #28-2 \t: jomleyeBazgasht -> RETURN_KW ebarat NOGHTE_VIRGUL')


def p_jomleyeShekast(p):
    """ jomleyeShekast : BREAK_KW NOGHTE_VIRGUL """
    # print('Rule #29 \t: jomleyeShekast -> BREAK_KW NOGHTE_VIRGUL')


def p_ebarat_1(p):
    """ ebarat : taghirpazir EQUALS ebarat """
    # print('Rule #30-1 \t: ebarat -> taghirpazir EQUALS ebarat')
    if p[1].type == p[3].type:
        qr.add(p[1], '=', p[3])
    else:
        raise Exception('type mismatch error near ' + p[1].place + ' = ' + p[3].place)


# TODO correct += and others
def p_ebarat_2(p):
    """ ebarat : taghirpazir PLUS_EQ ebarat """
    # print('Rule #30-2 \t: ebarat -> taghirpazir PLUS_EQ ebarat')
    if p[1].type == p[3].type:
        p[0] = Var(place=p[1].place + '+' + p[3].place, type=p[1].type)
        p[0].set_unique()
        qr.add(p[0], '+', p[1], p[3])
    else:
        raise Exception('type mismatch error near ' + p[1].place + ' += ' + p[3].place)


def p_ebarat_3(p):
    """ ebarat : taghirpazir MINUS_EQ ebarat """
    # print('Rule #30-3 \t: ebarat -> taghirpazir MINUS_EQ ebarat')
    if p[1].type == p[3].type:
        p[0] = Var(place=p[1].place + '-' + p[3].place, type=p[1].type)
        p[0].set_unique()
        qr.add(p[0], '-', p[1], p[3])
    else:
        raise Exception('type mismatch error near ' + p[1].place + ' -= ' + p[3].place)


def p_ebarat_4(p):
    """ ebarat : taghirpazir TIMES_EQ ebarat """
    # print('Rule #30-4 \t: ebarat -> taghirpazir TIMES_EQ ebarat')
    if p[1].type == p[3].type:
        p[0] = Var(place=p[1].place + '*' + p[3].place, type=p[1].type)
        p[0].set_unique()
        qr.add(p[0], '*', p[1], p[3])
    else:
        raise Exception('type mismatch error near ' + p[1].place + ' *= ' + p[3].place)


def p_ebarat_5(p):
    """ ebarat : taghirpazir DIVIDE_EQ ebarat """
    # print('Rule #30-5 \t: ebarat -> taghirpazir DIVIDE_EQ ebarat')
    if p[1].type == p[3].type:
        p[0] = Var(place=p[1].place + '/' + p[3].place, type=p[1].type)
        p[0].set_unique()
        qr.add(p[0], '/', p[1], p[3])
    else:
        raise Exception('type mismatch error near ' + p[1].place + ' /= ' + p[3].place)


def p_ebarat_6(p):
    """ ebarat : taghirpazir PLUS_PLUS """
    # print('Rule #30-6 \t: ebarat -> taghirpazir PLUS_PLUS')
    p[0] = Var(place=p[1].place + '++')
    qr.add(p[0], '++')


def p_ebarat_7(p):
    """ ebarat : taghirpazir MINUS_MINUS """
    # print('Rule #30-7 \t: ebarat -> taghirpazir MINUS_MINUS')
    p[0] = Var(place=p[1].place + '--')
    qr.add(p[0], '--')


def p_ebarat_8(p):
    """ ebarat : ebarateSade """
    # print('Rule #30-8 \t: ebarat -> ebarateSade')
    p[0] = p[1]


def p_ebarateSade_1(p):
    """ ebarateSade : ebarateSade OR_KW ebarateSade """
    # print('Rule #31-1 \t: ebarateSade -> ebarateSade OR_KW ebarateSade')
    p[0] = Var(place=p[1].place + '||' + p[3].place, type='bool')
    p[0].set_unique()
    qr.add(p[0], '||', p[1], p[3])


def p_ebarateSade_2(p):
    """ ebarateSade : ebarateSade AND_KW ebarateSade """
    # print('Rule #31-2 \t: ebarateSade -> ebarateSade AND_KW ebarateSade')
    p[0] = Var(place=p[1].place + '&&' + p[3].place, type='bool')
    p[0].set_unique()
    qr.add(p[0], '&&', p[1], p[3])


def p_ebarateSade_3(p):
    """ ebarateSade : ebarateSade SHORT_CIRCUIT_OR_KW ebarateSade """
    # print('Rule #31-3 \t: ebarateSade -> ebarateSade SHORT_CIRCUIT_OR_KW ebarateSade')
    p[0] = Var(place=p[1].place + '|' + p[3].place, type='bool')
    p[0].set_unique()
    qr.add(p[0], '|', p[1], p[3])


def p_ebarateSade_4(p):
    """ ebarateSade : ebarateSade SHORT_CIRCUIT_AND_KW ebarateSade """
    # print('Rule #31-4 \t: ebarateSade -> ebarateSade SHORT_CIRCUIT_AND_KW ebarateSade')
    p[0] = Var(place=p[1].place + '&' + p[3].place, type='bool')
    p[0].set_unique()
    qr.add(p[0], '&', p[1], p[3])


def p_ebarateSade_5(p):
    """ ebarateSade : NOT_KW ebarateSade """
    # print('Rule #31-5 \t: ebarateSade -> NOT_KW ebarateSade')
    p[0] = Var(place='!' + p[2].place, type='bool')
    p[0].set_unique()
    qr.add(p[0], '!', p[1])


def p_ebarateSade_6(p):
    """ ebarateSade : ebarateRabetei """
    # print('Rule #31-6 \t: ebarateSade -> ebarateRabetei')
    p[0] = p[1]


def p_ebarateRabetei_1(p):
    """ ebarateRabetei : ebarateRiaziManteghi """
    # print('Rule #32-1 \t: ebarateRabetei -> ebarateRiaziManteghi')
    p[0] = p[1]


def p_ebarateRabetei_2(p):
    """ ebarateRabetei : ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi """
    # print('Rule #32-2 \t: ebarateRabetei -> ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi')
    # if p[1].type == p[3].type:
    if True:  # TODO type checking
        p[0] = Var(place=p[1].place + p[2].op + p[3].place, type=p[1].type)
        p[0].set_unique()
        qr.add(p[0], p[2].op, p[1], p[3])
    else:
        raise Exception('type mismatch error near ' + p[1].place + p[2].op + p[3].place)


def p_amalgareRabetei_1(p):
    """ amalgareRabetei : LT  """
    # print('Rule #33-1 \t: amalgareRabetei -> LT')
    p[0] = Operator('<')


def p_amalgareRabetei_2(p):
    """ amalgareRabetei : GT  """
    # print('Rule #33-2 \t: amalgareRabetei -> GT')
    p[0] = Operator('>')


def p_amalgareRabetei_3(p):
    """ amalgareRabetei : GE """
    # print('Rule #33-3 \t: amalgareRabetei -> GE')
    p[0] = Operator('>=')


def p_amalgareRabetei_4(p):
    """ amalgareRabetei : LE """
    # print('Rule #33-4 \t: amalgareRabetei -> LE')
    p[0] = Operator('<=')


def p_amalgareRabetei_5(p):
    """ amalgareRabetei : EQ """
    # print('Rule #33-5 \t: amalgareRabetei -> EQ')
    p[0] = Operator('==')


def p_ebarateRiaziManteghi_1(p):
    """ ebarateRiaziManteghi : ebarateYegani """
    # print('Rule #34-1 \t: ebarateRiaziManteghi -> ebarateYegani')
    p[0] = p[1]


def p_ebarateRiaziManteghi_2(p):
    """ebarateRiaziManteghi : ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi """
    # print('Rule #34-2 \t: ebarateRiaziManteghi -> ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi')
    if p[1].type == p[3].type:
        p[0] = Var(place=p[1].place + p[2].op + p[3].place, type=p[1].type)
        p[0].set_unique()
        qr.add(p[0], p[2].op, p[1], p[3])
    else:
        raise Exception('type mismatch error near ' + p[1].place + p[2].op + p[3].place)


def p_amalgareRiazi_1(p):
    """ amalgareRiazi : PLUS """
    # print('Rule #35-1 \t: amalgareRiazi -> PLUS')
    p[0] = Operator('+')


def p_amalgareRiazi_2(p):
    """ amalgareRiazi : MINUS """
    # print('Rule #35-2 \t: amalgareRiazi -> MINUS')
    p[0] = Operator('-')


def p_amalgareRiazi_3(p):
    """ amalgareRiazi : TIMES """
    # print('Rule #35-3 \t: amalgareRiazi -> TIMES')
    p[0] = Operator('*')


def p_amalgareRiazi_4(p):
    """ amalgareRiazi : DIVIDE """
    # print('Rule #35-4 \t: amalgareRiazi -> DIVIDE')
    p[0] = Operator('/')


def p_amalgareRiazi_5(p):
    """ amalgareRiazi : MOD """
    # print('Rule #35-5 \t: amalgareRiazi -> MOD')
    p[0] = Operator('%')


def p_ebarateYegani_1(p):
    """ ebarateYegani : amalgareYegani ebarateYegani """
    # print('Rule #36-1 \t: ebarateYegani -> amalgareYegani ebarateYegani')
    p[0] = p[2]  # TODO add amalgareYegani


def p_ebarateYegani_2(p):
    """ ebarateYegani : amel """
    # print('Rule #36-2 \t: ebarateYegani -> amel')
    p[0] = p[1]


def p_amalgareYegani_1(p):
    """ amalgareYegani : MINUS """
    # print('Rule #37-1 \t: amalgareYegani -> MINUS')
    p[0] = Operator('')  # TODO correct this


def p_amalgareYegani_2(p):
    """ amalgareYegani : TIMES """
    # print('Rule #37-2 \t: amalgareYegani -> TIMES')
    p[0] = Operator('')  # TODO correct this


def p_amalgareYegani_3(p):
    """ amalgareYegani : QUESTION_MARK """
    # print('Rule #37-3 \t: amalgareYegani -> QUESTION_MARK')
    p[0] = Operator('')  # TODO correct this


def p_amel_1(p):
    """ amel : taghirpazir """
    # print('Rule #38-1 \t: amel -> taghirpazir')
    p[0] = p[1]


def p_amel_2(p):
    """ amel :  taghirnapazir """
    # print('Rule #38-2 \t: amel -> taghirnapazir')
    p[0] = p[1]


def p_taghirpazir_1(p):
    """ taghirpazir : SHENASE """
    # print('Rule #39-1 \t: taghirpazir -> SHENASE')
    p[0] = var[p[1]]


def p_taghirpazir_2(p):
    """ taghirpazir : taghirpazir OPEN_BRACKET ebarat CLOSE_BRACKET """
    # print('Rule #39-2 \t: taghirpazir -> taghirpazir OPEN_BRACKET ebarat CLOSE_BRACKET')


def p_taghirpazir_3(p):
    """taghirpazir : taghirpazir DOT SHENASE """
    # print('Rule #39-3 \t: taghirpazir -> taghirpazir DOT SHENASE')


def p_taghirnapazir_1(p):
    """ taghirnapazir : OPEN_PAREN ebarat CLOSE_PAREN """
    # print('Rule #40-1 \t: taghirnapazir -> OPEN_PAREN ebarat CLOSE_PAREN')


def p_taghirnapazir_2(p):
    """ taghirnapazir : sedaZadan """
    # print('Rule #40-2 \t: taghirnapazir -> sedaZadan')


def p_taghirnapazir_3(p):
    """taghirnapazir : meghdareSabet """
    # print('Rule #40-3 \t: taghirnapazir -> meghdarSabet')
    p[0] = p[1]


def p_sedaZadan(p):
    """ sedaZadan : SHENASE OPEN_PAREN bordareVorudi CLOSE_PAREN """
    # print('Rule #40 \t: sedaZadan -> SHENASE OPEN_PAREN bordareVorudi CLOSE_PAREN ')


def p_bordareVorudi_1(p):
    """ bordareVorudi : bordareVorudiha """
    # print('Rule #41-1 \t: bordareVorudi -> bordareVorudiha')


def p_bordareVorudi_2(p):
    """ bordareVorudi : epsilon """
    # print('Rule #41-2 \t: bordareVorudi -> epsilon ')


def p_bordareVorudiha_1(p):
    """ bordareVorudiha : bordareVorudiha COMMA ebarat """
    # print('Rule #42-1 \t:s bordareVorudiha -> bordareVorudiha COMMA ebarat')


def p_bordareVorudiha_2(p):
    """bordareVorudiha : ebarat """
    # print('Rule #42-2 \t: bordareVorudiha -> ebarat')


def p_meghdareSabet_1(p):
    """ meghdareSabet : INT """
    # print('Rule #43-1 \t: meghdareSabet -> INT ')
    p[0] = Var(place=str(p[1]), type='int', value=p[1])
    p[0].unique = p[0].place


def p_meghdareSabet_2(p):
    """ meghdareSabet :  FLOAT """
    # print('Rule #43-2 \t: meghdareSabet -> FLOAT ')
    p[0] = Var(place=str(p[1]), type='float', value=p[1])
    p[0].unique = p[0].place


def p_meghdareSabet_3(p):
    """ meghdareSabet :  HARFE_SABET """
    # print('Rule #43-3 \t: meghdareSabet -> HARFE_SABET ')
    p[0] = Var(place=str(p[1]), type='char', value=p[1])
    p[0].unique = p[0].place


def p_meghdareSabet_4(p):
    """ meghdareSabet : TRUE_KW """
    # print('Rule #43-4 \t: meghdareSabet -> TRUE_KW ')
    p[0] = Var(place=str(p[1]), type='bool', value=p[1])
    p[0].unique = p[0].place


def p_meghdareSabet_5(p):
    """ meghdareSabet : FALSE_KW """
    # print('Rule #43-5 \t: meghdareSabet -> FALSE_KW ')
    p[0] = Var(place=str(p[1]), type='bool', value=p[1])
    p[0].unique = p[0].place


def p_epsilon(p):
    """ epsilon : """


def p_error(p):
    if p:
        print('Syntax Error')
        print(p)
    else:
        print('Syntax Error EOF')


tokens = lex.tokens

parser = yacc.yacc()
