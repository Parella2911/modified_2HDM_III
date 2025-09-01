# This file was automatically created by FeynRules 2.3.31
# Mathematica version: 11.2.0 for Mac OS X x86 (64-bit) (September 11, 2017)
# Date: Fri 4 May 2018 15:52:17


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_727_277,(0,0,1):C.R2GC_727_278,(0,1,0):C.R2GC_730_279,(0,1,1):C.R2GC_730_280,(0,2,0):C.R2GC_730_279,(0,2,1):C.R2GC_730_280,(0,3,0):C.R2GC_727_277,(0,3,1):C.R2GC_727_278,(0,4,0):C.R2GC_727_277,(0,4,1):C.R2GC_727_278,(0,5,0):C.R2GC_730_279,(0,5,1):C.R2GC_730_280})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_585_144,(2,0,1):C.R2GC_585_145,(0,0,0):C.R2GC_585_144,(0,0,1):C.R2GC_585_145,(6,0,0):C.R2GC_588_149,(6,0,1):C.R2GC_737_286,(4,0,0):C.R2GC_583_140,(4,0,1):C.R2GC_583_141,(3,0,0):C.R2GC_583_140,(3,0,1):C.R2GC_583_141,(8,0,0):C.R2GC_584_142,(8,0,1):C.R2GC_584_143,(7,0,0):C.R2GC_589_151,(7,0,1):C.R2GC_736_285,(5,0,0):C.R2GC_583_140,(5,0,1):C.R2GC_583_141,(1,0,0):C.R2GC_583_140,(1,0,1):C.R2GC_583_141,(11,0,0):C.R2GC_587_147,(11,0,1):C.R2GC_587_148,(10,0,0):C.R2GC_587_147,(10,0,1):C.R2GC_587_148,(9,0,1):C.R2GC_586_146,(2,1,0):C.R2GC_585_144,(2,1,1):C.R2GC_585_145,(0,1,0):C.R2GC_585_144,(0,1,1):C.R2GC_585_145,(4,1,0):C.R2GC_583_140,(4,1,1):C.R2GC_583_141,(3,1,0):C.R2GC_583_140,(3,1,1):C.R2GC_583_141,(8,1,0):C.R2GC_584_142,(8,1,1):C.R2GC_738_287,(6,1,0):C.R2GC_733_281,(6,1,1):C.R2GC_733_282,(7,1,0):C.R2GC_589_151,(7,1,1):C.R2GC_589_152,(5,1,0):C.R2GC_583_140,(5,1,1):C.R2GC_583_141,(1,1,0):C.R2GC_583_140,(1,1,1):C.R2GC_583_141,(11,1,0):C.R2GC_587_147,(11,1,1):C.R2GC_587_148,(10,1,0):C.R2GC_587_147,(10,1,1):C.R2GC_587_148,(9,1,1):C.R2GC_586_146,(2,2,0):C.R2GC_585_144,(2,2,1):C.R2GC_585_145,(0,2,0):C.R2GC_585_144,(0,2,1):C.R2GC_585_145,(4,2,0):C.R2GC_583_140,(4,2,1):C.R2GC_583_141,(3,2,0):C.R2GC_583_140,(3,2,1):C.R2GC_583_141,(8,2,0):C.R2GC_584_142,(8,2,1):C.R2GC_735_284,(6,2,0):C.R2GC_588_149,(6,2,1):C.R2GC_588_150,(7,2,0):C.R2GC_734_283,(7,2,1):C.R2GC_585_145,(5,2,0):C.R2GC_583_140,(5,2,1):C.R2GC_583_141,(1,2,0):C.R2GC_583_140,(1,2,1):C.R2GC_583_141,(11,2,0):C.R2GC_587_147,(11,2,1):C.R2GC_587_148,(10,2,0):C.R2GC_587_147,(10,2,1):C.R2GC_587_148,(9,2,1):C.R2GC_586_146})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.d__tilde__, P.u, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_718_267,(0,1,0):C.R2GC_713_262})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.s__tilde__, P.u, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.g, P.s, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_724_273,(0,1,0):C.R2GC_719_268})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.u, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_700_249,(0,1,0):C.R2GC_693_242})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.d__tilde__, P.c, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_650_199,(0,1,0):C.R2GC_645_194})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.s__tilde__, P.c, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_656_205,(0,1,0):C.R2GC_651_200})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.c, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_644_193,(0,1,0):C.R2GC_637_186})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.d__tilde__, P.t, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.d, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_800_340,(0,1,0):C.R2GC_742_288})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.s__tilde__, P.t, P.h__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_801_341,(0,1,0):C.R2GC_743_289})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.h__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_802_342,(0,1,0):C.R2GC_744_290})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_717_266,(0,1,0):C.R2GC_716_265})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_649_198,(0,1,0):C.R2GC_648_197})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.t__tilde__, P.d, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_785_325,(0,1,0):C.R2GC_775_315})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_723_272,(0,1,0):C.R2GC_722_271})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_655_204,(0,1,0):C.R2GC_654_203})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.s, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_786_326,(0,1,0):C.R2GC_778_318})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.u__tilde__, P.b, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_699_248,(0,1,0):C.R2GC_698_247})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.b, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_643_192,(0,1,0):C.R2GC_642_191})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_787_327,(0,1,0):C.R2GC_781_321})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.t__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_777_317})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.t__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_780_320})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_697_246})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.c__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_641_190})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_783_323,(0,1,0):C.R2GC_784_324})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_593_155})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.b__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_695_244})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.b__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_639_188})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.d__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_766_309})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.s__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_767_310})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_768_311,(0,1,0):C.R2GC_764_307})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_765_308})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_634_183,(0,1,0):C.R2GC_631_180})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_635_184,(0,1,0):C.R2GC_632_181})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_636_185,(0,1,0):C.R2GC_633_182})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.c__tilde__, P.u, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_710_259,(0,1,0):C.R2GC_701_250})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.c__tilde__, P.u, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_711_260,(0,1,0):C.R2GC_703_252})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.u, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_712_261,(0,1,0):C.R2GC_705_254})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.u, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_794_334,(0,1,0):C.R2GC_752_295})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.u, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_795_335,(0,1,0):C.R2GC_756_299})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.u, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_796_336,(0,1,0):C.R2GC_760_303})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.u__tilde__, P.c, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_707_256,(0,1,0):C.R2GC_702_251})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.u__tilde__, P.c, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_708_257,(0,1,0):C.R2GC_704_253})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.u__tilde__, P.c, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_709_258,(0,1,0):C.R2GC_706_255})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_606_165,(0,1,0):C.R2GC_603_162})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_607_166,(0,1,0):C.R2GC_604_163})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_608_167,(0,1,0):C.R2GC_605_164})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.t__tilde__, P.c, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_797_337,(0,1,0):C.R2GC_753_296})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.t__tilde__, P.c, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_798_338,(0,1,0):C.R2GC_757_300})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.t__tilde__, P.c, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_799_339,(0,1,0):C.R2GC_761_304})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.t, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_788_328,(0,1,0):C.R2GC_754_297})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.u__tilde__, P.t, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_789_329,(0,1,0):C.R2GC_758_301})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.u__tilde__, P.t, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_790_330,(0,1,0):C.R2GC_762_305})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.c__tilde__, P.t, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_791_331,(0,1,0):C.R2GC_755_298})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.c__tilde__, P.t, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_792_332,(0,1,0):C.R2GC_759_302})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.c__tilde__, P.t, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_793_333,(0,1,0):C.R2GC_763_306})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_803_343,(0,1,0):C.R2GC_770_312})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_804_344,(0,1,0):C.R2GC_772_313})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_805_345,(0,1,0):C.R2GC_774_314})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_615_171,(0,1,0):C.R2GC_612_168})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_616_172,(0,1,0):C.R2GC_613_169})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_617_173,(0,1,0):C.R2GC_614_170})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.d, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_678_227,(0,1,0):C.R2GC_669_218})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.s__tilde__, P.d, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_679_228,(0,1,0):C.R2GC_671_220})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.s__tilde__, P.d, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_680_229,(0,1,0):C.R2GC_673_222})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.b__tilde__, P.d, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_666_215,(0,1,0):C.R2GC_657_206})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.b__tilde__, P.d, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_667_216,(0,1,0):C.R2GC_659_208})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.b__tilde__, P.d, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_668_217,(0,1,0):C.R2GC_661_210})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.d__tilde__, P.s, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_675_224,(0,1,0):C.R2GC_670_219})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.d__tilde__, P.s, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_676_225,(0,1,0):C.R2GC_672_221})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.d__tilde__, P.s, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_677_226,(0,1,0):C.R2GC_674_223})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_624_177,(0,1,0):C.R2GC_621_174})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_625_178,(0,1,0):C.R2GC_622_175})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_626_179,(0,1,0):C.R2GC_623_176})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.b__tilde__, P.s, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_690_239,(0,1,0):C.R2GC_681_230})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.b__tilde__, P.s, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_691_240,(0,1,0):C.R2GC_683_232})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.b__tilde__, P.s, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_692_241,(0,1,0):C.R2GC_685_234})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.d__tilde__, P.b, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_663_212,(0,1,0):C.R2GC_658_207})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.d__tilde__, P.b, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_664_213,(0,1,0):C.R2GC_660_209})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.d__tilde__, P.b, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_665_214,(0,1,0):C.R2GC_662_211})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.s__tilde__, P.b, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_687_236,(0,1,0):C.R2GC_682_231})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.s__tilde__, P.b, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_688_237,(0,1,0):C.R2GC_684_233})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.s__tilde__, P.b, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_689_238,(0,1,0):C.R2GC_686_235})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_597_159,(0,1,0):C.R2GC_594_156})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_598_160,(0,1,0):C.R2GC_595_157})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_599_161,(0,1,0):C.R2GC_596_158})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_558_34,(0,1,0):C.R2GC_533_4})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_558_34,(0,1,0):C.R2GC_533_4})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_558_34,(0,1,0):C.R2GC_533_4})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_556_32,(0,1,0):C.R2GC_531_2})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_556_32,(0,1,0):C.R2GC_531_2})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_556_32,(0,1,0):C.R2GC_531_2})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_592_154})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_592_154})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_592_154})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_592_154})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_592_154})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_592_154})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_714_263})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_720_269})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_694_243})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_646_195})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_652_201})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_638_187})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_745_291})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_746_292})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_747_293})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_715_264})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_647_196})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_776_316})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_721_270})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_653_202})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_779_319})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_696_245})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_640_189})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_782_322})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_557_33,(0,1,0):C.R2GC_534_5})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_557_33,(0,1,0):C.R2GC_534_5})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_557_33,(0,1,0):C.R2GC_534_5})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_555_31,(0,1,0):C.R2GC_532_3})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_555_31,(0,1,0):C.R2GC_532_3})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_555_31,(0,1,0):C.R2GC_532_3})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_590_153})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_590_153})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_748_294,(0,2,0):C.R2GC_748_294,(0,1,0):C.R2GC_590_153,(0,3,0):C.R2GC_590_153})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_590_153})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_590_153})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_590_153})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                 couplings = {(0,0,1):C.R2GC_726_276,(0,1,2):C.R2GC_530_1,(0,2,0):C.R2GC_725_274,(0,2,1):C.R2GC_725_275})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_542_8})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_543_9})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_544_10})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_552_25,(0,0,1):C.R2GC_552_26,(0,1,0):C.R2GC_552_25,(0,1,1):C.R2GC_552_26,(0,2,0):C.R2GC_552_25,(0,2,1):C.R2GC_552_26})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_553_27,(0,0,1):C.R2GC_553_28,(0,1,0):C.R2GC_553_27,(0,1,1):C.R2GC_553_28,(0,2,0):C.R2GC_553_27,(0,2,1):C.R2GC_553_28})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_554_29,(0,0,1):C.R2GC_554_30,(0,1,0):C.R2GC_554_29,(0,1,1):C.R2GC_554_30,(0,2,0):C.R2GC_554_29,(0,2,1):C.R2GC_554_30})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_568_50,(0,0,1):C.R2GC_568_51,(0,0,2):C.R2GC_568_52,(0,0,3):C.R2GC_568_53,(0,0,4):C.R2GC_568_54,(0,0,5):C.R2GC_568_55,(0,0,6):C.R2GC_568_56,(0,0,7):C.R2GC_568_57,(0,0,8):C.R2GC_568_58,(0,1,0):C.R2GC_568_50,(0,1,1):C.R2GC_568_51,(0,1,2):C.R2GC_568_52,(0,1,3):C.R2GC_568_53,(0,1,4):C.R2GC_568_54,(0,1,5):C.R2GC_568_55,(0,1,6):C.R2GC_568_56,(0,1,7):C.R2GC_568_57,(0,1,8):C.R2GC_568_58,(0,2,0):C.R2GC_568_50,(0,2,1):C.R2GC_568_51,(0,2,2):C.R2GC_568_52,(0,2,3):C.R2GC_568_53,(0,2,4):C.R2GC_568_54,(0,2,5):C.R2GC_568_55,(0,2,6):C.R2GC_568_56,(0,2,7):C.R2GC_568_57,(0,2,8):C.R2GC_568_58})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(1,0,0):C.R2GC_549_19,(1,0,1):C.R2GC_549_20,(0,1,0):C.R2GC_548_17,(0,1,1):C.R2GC_548_18,(0,2,0):C.R2GC_548_17,(0,2,1):C.R2GC_548_18,(0,3,0):C.R2GC_548_17,(0,3,1):C.R2GC_548_18})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)', 'f(2,3,4)' ],
                 lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(1,0,0):C.R2GC_551_23,(1,0,1):C.R2GC_551_24,(0,1,0):C.R2GC_550_21,(0,1,1):C.R2GC_550_22,(0,2,0):C.R2GC_550_21,(0,2,1):C.R2GC_550_22,(0,3,0):C.R2GC_550_21,(0,3,1):C.R2GC_550_22})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_541_6,(0,0,1):C.R2GC_541_7})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.d, P.t] ], [ [P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_564_40,(0,0,1):C.R2GC_564_41,(0,0,2):C.R2GC_564_42,(0,0,3):C.R2GC_564_43,(0,0,4):C.R2GC_564_44})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.d, P.t] ], [ [P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_565_45,(0,0,1):C.R2GC_565_46,(0,0,2):C.R2GC_565_47,(0,0,3):C.R2GC_565_48,(0,0,4):C.R2GC_565_49})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__plus__, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.d, P.t] ], [ [P.s, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_563_35,(0,0,1):C.R2GC_563_36,(0,0,2):C.R2GC_563_37,(0,0,3):C.R2GC_563_38,(0,0,4):C.R2GC_563_39})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h__minus__, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.c] ], [ [P.b, P.t] ], [ [P.b, P.u] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.t] ], [ [P.d, P.u] ], [ [P.s, P.t] ], [ [P.s, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_569_59,(0,0,1):C.R2GC_569_60,(0,0,2):C.R2GC_569_61,(0,0,3):C.R2GC_569_62,(0,0,4):C.R2GC_569_63,(0,0,5):C.R2GC_569_64,(0,0,6):C.R2GC_569_65,(0,0,7):C.R2GC_569_66,(0,0,8):C.R2GC_569_67})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_545_11,(0,0,1):C.R2GC_545_12})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h1, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.d] ], [ [P.b, P.s] ], [ [P.c] ], [ [P.c, P.t] ], [ [P.c, P.u] ], [ [P.d] ], [ [P.d, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.u] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_570_68,(0,0,3):C.R2GC_570_69,(0,0,6):C.R2GC_570_70,(0,0,8):C.R2GC_570_71,(0,0,9):C.R2GC_570_72,(0,0,11):C.R2GC_570_73,(0,0,1):C.R2GC_570_74,(0,0,2):C.R2GC_570_75,(0,0,4):C.R2GC_570_76,(0,0,5):C.R2GC_570_77,(0,0,7):C.R2GC_570_78,(0,0,10):C.R2GC_570_79})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_546_13,(0,0,1):C.R2GC_546_14})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h1, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.d] ], [ [P.b, P.s] ], [ [P.c] ], [ [P.c, P.t] ], [ [P.c, P.u] ], [ [P.d] ], [ [P.d, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.u] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_571_80,(0,0,3):C.R2GC_571_81,(0,0,6):C.R2GC_571_82,(0,0,8):C.R2GC_571_83,(0,0,9):C.R2GC_571_84,(0,0,11):C.R2GC_571_85,(0,0,1):C.R2GC_571_86,(0,0,2):C.R2GC_571_87,(0,0,4):C.R2GC_571_88,(0,0,5):C.R2GC_571_89,(0,0,7):C.R2GC_571_90,(0,0,10):C.R2GC_571_91})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h2, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.d] ], [ [P.b, P.s] ], [ [P.c] ], [ [P.c, P.t] ], [ [P.c, P.u] ], [ [P.d] ], [ [P.d, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.u] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_572_92,(0,0,3):C.R2GC_572_93,(0,0,6):C.R2GC_572_94,(0,0,8):C.R2GC_572_95,(0,0,9):C.R2GC_572_96,(0,0,11):C.R2GC_572_97,(0,0,1):C.R2GC_572_98,(0,0,2):C.R2GC_572_99,(0,0,4):C.R2GC_572_100,(0,0,5):C.R2GC_572_101,(0,0,7):C.R2GC_572_102,(0,0,10):C.R2GC_572_103})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_547_15,(0,0,1):C.R2GC_547_16})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h1, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.d] ], [ [P.b, P.s] ], [ [P.c] ], [ [P.c, P.t] ], [ [P.c, P.u] ], [ [P.d] ], [ [P.d, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.u] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_573_104,(0,0,3):C.R2GC_573_105,(0,0,6):C.R2GC_573_106,(0,0,8):C.R2GC_573_107,(0,0,9):C.R2GC_573_108,(0,0,11):C.R2GC_573_109,(0,0,1):C.R2GC_573_110,(0,0,2):C.R2GC_573_111,(0,0,4):C.R2GC_573_112,(0,0,5):C.R2GC_573_113,(0,0,7):C.R2GC_573_114,(0,0,10):C.R2GC_573_115})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h2, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.d] ], [ [P.b, P.s] ], [ [P.c] ], [ [P.c, P.t] ], [ [P.c, P.u] ], [ [P.d] ], [ [P.d, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.u] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_574_116,(0,0,3):C.R2GC_574_117,(0,0,6):C.R2GC_574_118,(0,0,8):C.R2GC_574_119,(0,0,9):C.R2GC_574_120,(0,0,11):C.R2GC_574_121,(0,0,1):C.R2GC_574_122,(0,0,2):C.R2GC_574_123,(0,0,4):C.R2GC_574_124,(0,0,5):C.R2GC_574_125,(0,0,7):C.R2GC_574_126,(0,0,10):C.R2GC_574_127})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.g, P.g, P.h3, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.d] ], [ [P.b, P.s] ], [ [P.c] ], [ [P.c, P.t] ], [ [P.c, P.u] ], [ [P.d] ], [ [P.d, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.u] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_575_128,(0,0,3):C.R2GC_575_129,(0,0,6):C.R2GC_575_130,(0,0,8):C.R2GC_575_131,(0,0,9):C.R2GC_575_132,(0,0,11):C.R2GC_575_133,(0,0,1):C.R2GC_575_134,(0,0,2):C.R2GC_575_135,(0,0,4):C.R2GC_575_136,(0,0,5):C.R2GC_575_137,(0,0,7):C.R2GC_575_138,(0,0,10):C.R2GC_575_139})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_727_236,(0,0,1):C.UVGC_727_237,(0,0,2):C.UVGC_582_5,(0,0,3):C.UVGC_727_238,(0,1,0):C.UVGC_730_243,(0,1,1):C.UVGC_730_244,(0,1,2):C.UVGC_730_245,(0,1,3):C.UVGC_730_246,(0,3,0):C.UVGC_730_243,(0,3,1):C.UVGC_732_249,(0,3,2):C.UVGC_581_3,(0,3,3):C.UVGC_730_246,(0,5,0):C.UVGC_727_236,(0,5,1):C.UVGC_729_241,(0,5,2):C.UVGC_729_242,(0,5,3):C.UVGC_727_238,(0,6,0):C.UVGC_727_236,(0,6,1):C.UVGC_728_239,(0,6,2):C.UVGC_728_240,(0,6,3):C.UVGC_727_238,(0,7,0):C.UVGC_730_243,(0,7,1):C.UVGC_731_247,(0,7,2):C.UVGC_731_248,(0,7,3):C.UVGC_730_246,(0,2,1):C.UVGC_581_2,(0,2,2):C.UVGC_581_3,(0,4,1):C.UVGC_582_4,(0,4,2):C.UVGC_582_5})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(2,0,2):C.UVGC_584_9,(2,0,3):C.UVGC_584_8,(0,0,2):C.UVGC_584_9,(0,0,3):C.UVGC_584_8,(6,0,1):C.UVGC_736_259,(6,0,2):C.UVGC_737_263,(6,0,3):C.UVGC_737_264,(6,0,4):C.UVGC_736_262,(4,0,2):C.UVGC_583_6,(4,0,3):C.UVGC_583_7,(3,0,2):C.UVGC_583_6,(3,0,3):C.UVGC_583_7,(8,0,2):C.UVGC_584_8,(8,0,3):C.UVGC_584_9,(7,0,1):C.UVGC_736_259,(7,0,2):C.UVGC_736_260,(7,0,3):C.UVGC_736_261,(7,0,4):C.UVGC_736_262,(5,0,2):C.UVGC_583_6,(5,0,3):C.UVGC_583_7,(1,0,2):C.UVGC_583_6,(1,0,3):C.UVGC_583_7,(11,0,2):C.UVGC_587_12,(11,0,3):C.UVGC_587_13,(10,0,2):C.UVGC_587_12,(10,0,3):C.UVGC_587_13,(9,0,2):C.UVGC_586_10,(9,0,3):C.UVGC_586_11,(2,1,2):C.UVGC_584_9,(2,1,3):C.UVGC_584_8,(0,1,2):C.UVGC_584_9,(0,1,3):C.UVGC_584_8,(4,1,2):C.UVGC_583_6,(4,1,3):C.UVGC_583_7,(3,1,2):C.UVGC_583_6,(3,1,3):C.UVGC_583_7,(8,1,1):C.UVGC_738_265,(8,1,2):C.UVGC_738_266,(8,1,3):C.UVGC_738_267,(8,1,4):C.UVGC_738_268,(6,1,2):C.UVGC_733_250,(6,1,3):C.UVGC_733_251,(6,1,4):C.UVGC_733_252,(7,1,0):C.UVGC_588_14,(7,1,2):C.UVGC_589_16,(7,1,3):C.UVGC_589_17,(5,1,2):C.UVGC_583_6,(5,1,3):C.UVGC_583_7,(1,1,2):C.UVGC_583_6,(1,1,3):C.UVGC_583_7,(11,1,2):C.UVGC_587_12,(11,1,3):C.UVGC_587_13,(10,1,2):C.UVGC_587_12,(10,1,3):C.UVGC_587_13,(9,1,2):C.UVGC_586_10,(9,1,3):C.UVGC_586_11,(2,2,2):C.UVGC_584_9,(2,2,3):C.UVGC_584_8,(0,2,2):C.UVGC_584_9,(0,2,3):C.UVGC_584_8,(4,2,2):C.UVGC_583_6,(4,2,3):C.UVGC_583_7,(3,2,2):C.UVGC_583_6,(3,2,3):C.UVGC_583_7,(8,2,1):C.UVGC_735_255,(8,2,2):C.UVGC_735_256,(8,2,3):C.UVGC_735_257,(8,2,4):C.UVGC_735_258,(6,2,0):C.UVGC_588_14,(6,2,2):C.UVGC_588_15,(6,2,3):C.UVGC_586_10,(7,2,2):C.UVGC_734_253,(7,2,3):C.UVGC_734_254,(7,2,4):C.UVGC_733_252,(5,2,2):C.UVGC_583_6,(5,2,3):C.UVGC_583_7,(1,2,2):C.UVGC_583_6,(1,2,3):C.UVGC_583_7,(11,2,2):C.UVGC_587_12,(11,2,3):C.UVGC_587_13,(10,2,2):C.UVGC_587_12,(10,2,3):C.UVGC_587_13,(9,2,2):C.UVGC_586_10,(9,2,3):C.UVGC_586_11})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_718_218,(0,0,1):C.UVGC_718_219,(0,1,0):C.UVGC_713_208,(0,1,1):C.UVGC_713_209})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_724_230,(0,0,1):C.UVGC_724_231,(0,1,0):C.UVGC_719_220,(0,1,1):C.UVGC_719_221})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_700_182,(0,0,1):C.UVGC_700_183,(0,1,0):C.UVGC_693_168,(0,1,1):C.UVGC_693_169})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_650_82,(0,0,0):C.UVGC_650_83,(0,1,1):C.UVGC_645_72,(0,1,0):C.UVGC_645_73})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_656_94,(0,0,1):C.UVGC_656_95,(0,1,0):C.UVGC_651_84,(0,1,1):C.UVGC_651_85})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_644_70,(0,0,0):C.UVGC_644_71,(0,1,1):C.UVGC_637_56,(0,1,0):C.UVGC_637_57})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_800_424,(0,0,2):C.UVGC_800_425,(0,0,1):C.UVGC_800_426,(0,1,0):C.UVGC_742_272,(0,1,2):C.UVGC_742_273,(0,1,1):C.UVGC_742_274})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_801_427,(0,0,2):C.UVGC_801_428,(0,0,1):C.UVGC_801_429,(0,1,0):C.UVGC_743_275,(0,1,2):C.UVGC_743_276,(0,1,1):C.UVGC_743_277})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_802_430,(0,0,2):C.UVGC_802_431,(0,0,1):C.UVGC_802_432,(0,1,0):C.UVGC_744_278,(0,1,2):C.UVGC_744_279,(0,1,1):C.UVGC_744_280})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_717_216,(0,0,1):C.UVGC_717_217,(0,1,0):C.UVGC_716_214,(0,1,1):C.UVGC_716_215})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_649_80,(0,0,0):C.UVGC_649_81,(0,1,1):C.UVGC_648_78,(0,1,0):C.UVGC_648_79})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_785_379,(0,0,2):C.UVGC_785_380,(0,0,1):C.UVGC_785_381,(0,1,0):C.UVGC_775_349,(0,1,2):C.UVGC_775_350,(0,1,1):C.UVGC_775_351})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_723_228,(0,0,1):C.UVGC_723_229,(0,1,0):C.UVGC_722_226,(0,1,1):C.UVGC_722_227})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_655_92,(0,0,1):C.UVGC_655_93,(0,1,0):C.UVGC_654_90,(0,1,1):C.UVGC_654_91})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_786_382,(0,0,2):C.UVGC_786_383,(0,0,1):C.UVGC_786_384,(0,1,0):C.UVGC_778_358,(0,1,2):C.UVGC_778_359,(0,1,1):C.UVGC_778_360})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_699_180,(0,0,1):C.UVGC_699_181,(0,1,0):C.UVGC_698_178,(0,1,1):C.UVGC_698_179})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_643_68,(0,0,0):C.UVGC_643_69,(0,1,1):C.UVGC_642_66,(0,1,0):C.UVGC_642_67})

V_172 = CTVertex(name = 'V_172',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_787_385,(0,0,2):C.UVGC_787_386,(0,0,1):C.UVGC_787_387,(0,1,0):C.UVGC_781_367,(0,1,2):C.UVGC_781_368,(0,1,1):C.UVGC_781_369})

V_173 = CTVertex(name = 'V_173',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_777_355,(0,0,2):C.UVGC_777_356,(0,0,1):C.UVGC_777_357})

V_174 = CTVertex(name = 'V_174',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_780_364,(0,0,2):C.UVGC_780_365,(0,0,1):C.UVGC_780_366})

V_175 = CTVertex(name = 'V_175',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_697_176,(0,0,1):C.UVGC_697_177})

V_176 = CTVertex(name = 'V_176',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_641_64,(0,0,0):C.UVGC_641_65})

V_177 = CTVertex(name = 'V_177',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_783_373,(0,0,2):C.UVGC_783_374,(0,0,1):C.UVGC_783_375,(0,1,0):C.UVGC_784_376,(0,1,2):C.UVGC_784_377,(0,1,1):C.UVGC_784_378})

V_178 = CTVertex(name = 'V_178',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_593_25})

V_179 = CTVertex(name = 'V_179',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_695_172,(0,0,1):C.UVGC_695_173})

V_180 = CTVertex(name = 'V_180',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_639_60,(0,0,0):C.UVGC_639_61})

V_181 = CTVertex(name = 'V_181',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_766_334,(0,0,2):C.UVGC_766_335,(0,0,1):C.UVGC_766_336})

V_182 = CTVertex(name = 'V_182',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_767_337,(0,0,2):C.UVGC_767_338,(0,0,1):C.UVGC_767_339})

V_183 = CTVertex(name = 'V_183',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_768_340,(0,0,2):C.UVGC_768_341,(0,0,1):C.UVGC_768_342,(0,1,0):C.UVGC_764_330,(0,1,2):C.UVGC_764_331,(0,1,1):C.UVGC_764_332})

V_184 = CTVertex(name = 'V_184',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_765_333})

V_185 = CTVertex(name = 'V_185',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_634_53,(0,1,0):C.UVGC_631_50})

V_186 = CTVertex(name = 'V_186',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_635_54,(0,1,0):C.UVGC_632_51})

V_187 = CTVertex(name = 'V_187',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_636_55,(0,1,0):C.UVGC_633_52})

V_188 = CTVertex(name = 'V_188',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.u, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.u] ], [ [P.c, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_710_202,(0,0,1):C.UVGC_710_203,(0,1,0):C.UVGC_701_184,(0,1,1):C.UVGC_701_185})

V_189 = CTVertex(name = 'V_189',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.u, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.u] ], [ [P.c, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_711_204,(0,0,1):C.UVGC_711_205,(0,1,0):C.UVGC_703_188,(0,1,1):C.UVGC_703_189})

V_190 = CTVertex(name = 'V_190',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.u, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.u] ], [ [P.c, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_712_206,(0,0,1):C.UVGC_712_207,(0,1,0):C.UVGC_705_192,(0,1,1):C.UVGC_705_193})

V_191 = CTVertex(name = 'V_191',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.u, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_794_406,(0,0,2):C.UVGC_794_407,(0,0,1):C.UVGC_794_408,(0,1,0):C.UVGC_752_294,(0,1,2):C.UVGC_752_295,(0,1,1):C.UVGC_752_296})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.u, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_795_409,(0,0,2):C.UVGC_795_410,(0,0,1):C.UVGC_795_411,(0,1,0):C.UVGC_756_306,(0,1,2):C.UVGC_756_307,(0,1,1):C.UVGC_756_308})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.u, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_796_412,(0,0,2):C.UVGC_796_413,(0,0,1):C.UVGC_796_414,(0,1,0):C.UVGC_760_318,(0,1,2):C.UVGC_760_319,(0,1,1):C.UVGC_760_320})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.c, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.u] ], [ [P.c, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_707_196,(0,0,1):C.UVGC_707_197,(0,1,0):C.UVGC_702_186,(0,1,1):C.UVGC_702_187})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.c, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.u] ], [ [P.c, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_708_198,(0,0,1):C.UVGC_708_199,(0,1,0):C.UVGC_704_190,(0,1,1):C.UVGC_704_191})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.c, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.u] ], [ [P.c, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_709_200,(0,0,1):C.UVGC_709_201,(0,1,0):C.UVGC_706_194,(0,1,1):C.UVGC_706_195})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_606_35,(0,1,0):C.UVGC_603_32})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_607_36,(0,1,0):C.UVGC_604_33})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_608_37,(0,1,0):C.UVGC_605_34})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.c, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_797_415,(0,0,2):C.UVGC_797_416,(0,0,1):C.UVGC_797_417,(0,1,0):C.UVGC_753_297,(0,1,2):C.UVGC_753_298,(0,1,1):C.UVGC_753_299})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.c, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_798_418,(0,0,2):C.UVGC_798_419,(0,0,1):C.UVGC_798_420,(0,1,0):C.UVGC_757_309,(0,1,2):C.UVGC_757_310,(0,1,1):C.UVGC_757_311})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.c, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_799_421,(0,0,2):C.UVGC_799_422,(0,0,1):C.UVGC_799_423,(0,1,0):C.UVGC_761_321,(0,1,2):C.UVGC_761_322,(0,1,1):C.UVGC_761_323})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.t, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_788_388,(0,0,2):C.UVGC_788_389,(0,0,1):C.UVGC_788_390,(0,1,0):C.UVGC_754_300,(0,1,2):C.UVGC_754_301,(0,1,1):C.UVGC_754_302})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.t, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_789_391,(0,0,2):C.UVGC_789_392,(0,0,1):C.UVGC_789_393,(0,1,0):C.UVGC_758_312,(0,1,2):C.UVGC_758_313,(0,1,1):C.UVGC_758_314})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.t, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_790_394,(0,0,2):C.UVGC_790_395,(0,0,1):C.UVGC_790_396,(0,1,0):C.UVGC_762_324,(0,1,2):C.UVGC_762_325,(0,1,1):C.UVGC_762_326})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.t, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_791_397,(0,0,2):C.UVGC_791_398,(0,0,1):C.UVGC_791_399,(0,1,0):C.UVGC_755_303,(0,1,2):C.UVGC_755_304,(0,1,1):C.UVGC_755_305})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.t, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_792_400,(0,0,2):C.UVGC_792_401,(0,0,1):C.UVGC_792_402,(0,1,0):C.UVGC_759_315,(0,1,2):C.UVGC_759_316,(0,1,1):C.UVGC_759_317})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.t, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_793_403,(0,0,2):C.UVGC_793_404,(0,0,1):C.UVGC_793_405,(0,1,0):C.UVGC_763_327,(0,1,2):C.UVGC_763_328,(0,1,1):C.UVGC_763_329})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2, L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_803_433,(0,2,0):C.UVGC_770_344,(0,0,0):C.UVGC_769_343})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2, L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_804_434,(0,2,0):C.UVGC_772_346,(0,0,0):C.UVGC_771_345})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2, L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_805_435,(0,2,0):C.UVGC_774_348,(0,0,0):C.UVGC_773_347})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_615_41,(0,1,0):C.UVGC_612_38})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_616_42,(0,1,0):C.UVGC_613_39})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_617_43,(0,1,0):C.UVGC_614_40})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.d, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.s] ], [ [P.d, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_678_138,(0,0,1):C.UVGC_678_139,(0,1,0):C.UVGC_669_120,(0,1,1):C.UVGC_669_121})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.d, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.s] ], [ [P.d, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_679_140,(0,0,1):C.UVGC_679_141,(0,1,0):C.UVGC_671_124,(0,1,1):C.UVGC_671_125})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.d, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.s] ], [ [P.d, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_680_142,(0,0,1):C.UVGC_680_143,(0,1,0):C.UVGC_673_128,(0,1,1):C.UVGC_673_129})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.d, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_666_114,(0,0,0):C.UVGC_666_115,(0,1,1):C.UVGC_657_96,(0,1,0):C.UVGC_657_97})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.d, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_667_116,(0,0,0):C.UVGC_667_117,(0,1,1):C.UVGC_659_100,(0,1,0):C.UVGC_659_101})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.d, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_668_118,(0,0,0):C.UVGC_668_119,(0,1,1):C.UVGC_661_104,(0,1,0):C.UVGC_661_105})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.s, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.s] ], [ [P.d, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_675_132,(0,0,1):C.UVGC_675_133,(0,1,0):C.UVGC_670_122,(0,1,1):C.UVGC_670_123})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.s, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.s] ], [ [P.d, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_676_134,(0,0,1):C.UVGC_676_135,(0,1,0):C.UVGC_672_126,(0,1,1):C.UVGC_672_127})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.s, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.s] ], [ [P.d, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_677_136,(0,0,1):C.UVGC_677_137,(0,1,0):C.UVGC_674_130,(0,1,1):C.UVGC_674_131})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_624_47,(0,1,0):C.UVGC_621_44})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_625_48,(0,1,0):C.UVGC_622_45})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_626_49,(0,1,0):C.UVGC_623_46})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.s, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.s] ], [ [P.b, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_690_162,(0,0,1):C.UVGC_690_163,(0,1,0):C.UVGC_681_144,(0,1,1):C.UVGC_681_145})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.s, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.s] ], [ [P.b, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_691_164,(0,0,1):C.UVGC_691_165,(0,1,0):C.UVGC_683_148,(0,1,1):C.UVGC_683_149})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.s, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.s] ], [ [P.b, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_692_166,(0,0,1):C.UVGC_692_167,(0,1,0):C.UVGC_685_152,(0,1,1):C.UVGC_685_153})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.b, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_663_108,(0,0,0):C.UVGC_663_109,(0,1,1):C.UVGC_658_98,(0,1,0):C.UVGC_658_99})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.b, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_664_110,(0,0,0):C.UVGC_664_111,(0,1,1):C.UVGC_660_102,(0,1,0):C.UVGC_660_103})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.b, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_665_112,(0,0,0):C.UVGC_665_113,(0,1,1):C.UVGC_662_106,(0,1,0):C.UVGC_662_107})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.b, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.s] ], [ [P.b, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_687_156,(0,0,1):C.UVGC_687_157,(0,1,0):C.UVGC_682_146,(0,1,1):C.UVGC_682_147})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.b, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.s] ], [ [P.b, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_688_158,(0,0,1):C.UVGC_688_159,(0,1,0):C.UVGC_684_150,(0,1,1):C.UVGC_684_151})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.b, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.s] ], [ [P.b, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_689_160,(0,0,1):C.UVGC_689_161,(0,1,0):C.UVGC_686_154,(0,1,1):C.UVGC_686_155})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_597_29,(0,1,0):C.UVGC_594_26})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_598_30,(0,1,0):C.UVGC_595_27})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_599_31,(0,1,0):C.UVGC_596_28})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_751_293,(0,1,0):C.UVGC_741_271})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                 couplings = {(0,0,3):C.UVGC_592_24,(0,1,0):C.UVGC_591_19,(0,1,1):C.UVGC_591_20,(0,1,2):C.UVGC_591_21,(0,1,4):C.UVGC_591_22,(0,1,3):C.UVGC_591_23,(0,2,0):C.UVGC_591_19,(0,2,1):C.UVGC_591_20,(0,2,2):C.UVGC_591_21,(0,2,4):C.UVGC_591_22,(0,2,3):C.UVGC_591_23})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,1):C.UVGC_592_24,(0,1,0):C.UVGC_591_19,(0,1,2):C.UVGC_591_20,(0,1,3):C.UVGC_591_21,(0,1,4):C.UVGC_591_22,(0,1,1):C.UVGC_591_23,(0,2,0):C.UVGC_591_19,(0,2,2):C.UVGC_591_20,(0,2,3):C.UVGC_591_21,(0,2,4):C.UVGC_591_22,(0,2,1):C.UVGC_591_23})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                 couplings = {(0,0,3):C.UVGC_592_24,(0,1,0):C.UVGC_591_19,(0,1,1):C.UVGC_591_20,(0,1,2):C.UVGC_591_21,(0,1,4):C.UVGC_591_22,(0,1,3):C.UVGC_740_270,(0,2,0):C.UVGC_591_19,(0,2,1):C.UVGC_591_20,(0,2,2):C.UVGC_591_21,(0,2,4):C.UVGC_591_22,(0,2,3):C.UVGC_740_270})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,1):C.UVGC_592_24,(0,1,0):C.UVGC_591_19,(0,1,2):C.UVGC_591_20,(0,1,3):C.UVGC_591_21,(0,1,4):C.UVGC_591_22,(0,1,1):C.UVGC_591_23,(0,2,0):C.UVGC_591_19,(0,2,2):C.UVGC_591_20,(0,2,3):C.UVGC_591_21,(0,2,4):C.UVGC_591_22,(0,2,1):C.UVGC_591_23})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                 couplings = {(0,0,3):C.UVGC_592_24,(0,1,0):C.UVGC_591_19,(0,1,1):C.UVGC_591_20,(0,1,2):C.UVGC_591_21,(0,1,4):C.UVGC_591_22,(0,1,3):C.UVGC_591_23,(0,2,0):C.UVGC_591_19,(0,2,1):C.UVGC_591_20,(0,2,2):C.UVGC_591_21,(0,2,4):C.UVGC_591_22,(0,2,3):C.UVGC_591_23})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,1):C.UVGC_592_24,(0,1,0):C.UVGC_591_19,(0,1,2):C.UVGC_591_20,(0,1,3):C.UVGC_591_21,(0,1,4):C.UVGC_591_22,(0,1,1):C.UVGC_591_23,(0,2,0):C.UVGC_591_19,(0,2,2):C.UVGC_591_20,(0,2,3):C.UVGC_591_21,(0,2,4):C.UVGC_591_22,(0,2,1):C.UVGC_591_23})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_714_210,(0,0,1):C.UVGC_714_211})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_720_222,(0,0,1):C.UVGC_720_223})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_694_170,(0,0,1):C.UVGC_694_171})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_646_74,(0,0,0):C.UVGC_646_75})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_652_86,(0,0,1):C.UVGC_652_87})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_638_58,(0,0,0):C.UVGC_638_59})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_745_281,(0,0,2):C.UVGC_745_282,(0,0,1):C.UVGC_745_283})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_746_284,(0,0,2):C.UVGC_746_285,(0,0,1):C.UVGC_746_286})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_747_287,(0,0,2):C.UVGC_747_288,(0,0,1):C.UVGC_747_289})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_715_212,(0,0,1):C.UVGC_715_213})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_647_76,(0,0,0):C.UVGC_647_77})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_776_352,(0,0,2):C.UVGC_776_353,(0,0,1):C.UVGC_776_354})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_721_224,(0,0,1):C.UVGC_721_225})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_653_88,(0,0,1):C.UVGC_653_89})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_779_361,(0,0,2):C.UVGC_779_362,(0,0,1):C.UVGC_779_363})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g], [P.g, P.u] ], [ [P.b, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_696_174,(0,0,1):C.UVGC_696_175})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.c, P.g] ], [ [P.b, P.g], [P.c, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_640_62,(0,0,0):C.UVGC_640_63})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_782_370,(0,0,2):C.UVGC_782_371,(0,0,1):C.UVGC_782_372})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_749_291,(0,1,0):C.UVGC_750_292})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_590_18,(0,1,0):C.UVGC_576_1,(0,2,0):C.UVGC_576_1})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_590_18,(0,1,0):C.UVGC_576_1,(0,2,0):C.UVGC_576_1})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_748_290,(0,2,0):C.UVGC_748_290,(0,1,0):C.UVGC_739_269,(0,3,0):C.UVGC_739_269})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_590_18,(0,1,0):C.UVGC_576_1,(0,2,0):C.UVGC_576_1})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_590_18,(0,1,0):C.UVGC_576_1,(0,2,0):C.UVGC_576_1})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_590_18,(0,1,0):C.UVGC_576_1,(0,2,0):C.UVGC_576_1})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_726_233,(0,0,1):C.UVGC_726_234,(0,0,2):C.UVGC_726_235,(0,1,2):C.UVGC_725_232})

