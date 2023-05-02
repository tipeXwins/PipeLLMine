46c46
<         super().__init__(qubit_count=None, ascii_symbols=["H"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["H"])
55,57d54
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
72c69
<         return [Instruction(H(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.H(), target=qubit) for qubit in QubitSet(target)]
82c79
<         super().__init__(qubit_count=None, ascii_symbols=["I"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["I"])
91,93d87
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
108c102
<         return [Instruction(I(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.I(), target=qubit) for qubit in QubitSet(target)]
118c112
<         super().__init__(qubit_count=None, ascii_symbols=["X"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["X"])
127,129d120
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
144c135
<         return [Instruction(X(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.X(), target=qubit) for qubit in QubitSet(target)]
154c145
<         super().__init__(qubit_count=None, ascii_symbols=["Y"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["Y"])
163,165d153
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
180c168
<         return [Instruction(Y(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.Y(), target=qubit) for qubit in QubitSet(target)]
190c178
<         super().__init__(qubit_count=None, ascii_symbols=["Z"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["Z"])
199,201d186
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
216c201
<         return [Instruction(Z(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.Z(), target=qubit) for qubit in QubitSet(target)]
226c211
<         super().__init__(qubit_count=None, ascii_symbols=["S"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["S"])
236,238d220
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
253c235
<         return [Instruction(S(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.S(), target=qubit) for qubit in QubitSet(target)]
263c245
<         super().__init__(qubit_count=None, ascii_symbols=["Si"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["Si"])
272,274d253
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
289c268
<         return [Instruction(Si(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.Si(), target=qubit) for qubit in QubitSet(target)]
299c278
<         super().__init__(qubit_count=None, ascii_symbols=["T"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["T"])
308,310d286
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
325c301
<         return [Instruction(T(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.T(), target=qubit) for qubit in QubitSet(target)]
335c311
<         super().__init__(qubit_count=None, ascii_symbols=["Ti"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["Ti"])
344,346d319
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
361c334
<         return [Instruction(Ti(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.Ti(), target=qubit) for qubit in QubitSet(target)]
371c344
<         super().__init__(qubit_count=None, ascii_symbols=["V"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["V"])
380,382d352
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
397c367
<         return [Instruction(V(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.V(), target=qubit) for qubit in QubitSet(target)]
407c377
<         super().__init__(qubit_count=None, ascii_symbols=["Vi"])
---
>         super().__init__(qubit_count=1, ascii_symbols=["Vi"])
416,418d385
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
433c400
<         return [Instruction(Vi(), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.Vi(), target=qubit) for qubit in QubitSet(target)]
450c417
<         super().__init__(angle=angle, qubit_count=None, ascii_symbols=["Rx({:.3g})".format(angle)])
---
>         super().__init__(angle=angle, qubit_count=1, ascii_symbols=["Rx({:.3g})".format(angle)])
461,463d427
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
465c429
<     def rx(target: QubitInput, angle: float) -> Iterable[Instruction]:
---
>     def rx(target: QubitInput, angle: float) -> Instruction:
473c437
<             Iterable[Instruction]: Rx instruction.
---
>             Instruction: Rx instruction.
478c442
<         return [Instruction(Rx(angle), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.Rx(angle), target=qubit) for qubit in QubitSet(target)]
492c456
<         super().__init__(angle=angle, qubit_count=None, ascii_symbols=["Ry({:.3g})".format(angle)])
---
>         super().__init__(angle=angle, qubit_count=1, ascii_symbols=["Ry({:.3g})".format(angle)])
503,505d466
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
507c468
<     def ry(target: QubitInput, angle: float) -> Iterable[Instruction]:
---
>     def ry(target: QubitInput, angle: float) -> Instruction:
515c476
<             Iterable[Instruction]: Ry instruction.
---
>             Instruction: Ry instruction.
520c481
<         return [Instruction(Ry(angle), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.Ry(angle), target=qubit) for qubit in QubitSet(target)]
534c495
<         super().__init__(angle=angle, qubit_count=None, ascii_symbols=["Rz({:.3g})".format(angle)])
---
>         super().__init__(angle=angle, qubit_count=1, ascii_symbols=["Rz({:.3g})".format(angle)])
545,547d505
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
549c507
<     def rz(target: QubitInput, angle: float) -> Iterable[Instruction]:
---
>     def rz(target: QubitInput, angle: float) -> Instruction:
557c515
<             Iterable[Instruction]: Rz instruction.
---
>             Instruction: Rz instruction.
562c520
<         return [Instruction(Rz(angle), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.Rz(angle), target=qubit) for qubit in QubitSet(target)]
576,578c534
<         super().__init__(
<             angle=angle, qubit_count=None, ascii_symbols=["PHASE({:.3g})".format(angle)]
<         )
---
>         super().__init__(angle=angle, qubit_count=1, ascii_symbols=["PHASE({:.3g})".format(angle)])
587,589d542
<     def fixed_qubit_count() -> int:
<         return 1
<     @staticmethod
591c544
<     def phaseshift(target: QubitInput, angle: float) -> Iterable[Instruction]:
---
>     def phaseshift(target: QubitInput, angle: float) -> Instruction:
599c552
<             Iterable[Instruction]: PhaseShift instruction.
---
>             Instruction: PhaseShift instruction.
604c557
<         return [Instruction(PhaseShift(angle), target=qubit) for qubit in QubitSet(target)]
---
>         return [Instruction(Gate.PhaseShift(angle), target=qubit) for qubit in QubitSet(target)]
617c570
<         super().__init__(qubit_count=None, ascii_symbols=["C", "X"])
---
>         super().__init__(qubit_count=2, ascii_symbols=["C", "X"])
634,636d586
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
651c601
<         return Instruction(CNot(), target=[control, target])
---
>         return Instruction(Gate.CNot(), target=[control, target])
661c611
<         super().__init__(qubit_count=None, ascii_symbols=["SWAP", "SWAP"])
---
>         super().__init__(qubit_count=2, ascii_symbols=["SWAP", "SWAP"])
678,680d627
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
695c642
<         return Instruction(Swap(), target=[target1, target2])
---
>         return Instruction(Gate.Swap(), target=[target1, target2])
705c652
<         super().__init__(qubit_count=None, ascii_symbols=["ISWAP", "ISWAP"])
---
>         super().__init__(qubit_count=2, ascii_symbols=["ISWAP", "ISWAP"])
722,724d668
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
739c683
<         return Instruction(ISwap(), target=[target1, target2])
---
>         return Instruction(Gate.ISwap(), target=[target1, target2])
755c699
<             qubit_count=None,
---
>             qubit_count=2,
774,776d717
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
791c732
<         return Instruction(PSwap(angle), target=[target1, target2])
---
>         return Instruction(Gate.PSwap(angle), target=[target1, target2])
809c750
<             qubit_count=None,
---
>             qubit_count=2,
830,832d770
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
847c785
<         return Instruction(XY(angle), target=[target1, target2])
---
>         return Instruction(Gate.XY(angle), target=[target1, target2])
862c800
<             angle=angle, qubit_count=None, ascii_symbols=["C", "PHASE({:.3g})".format(angle)]
---
>             angle=angle, qubit_count=2, ascii_symbols=["C", "PHASE({:.3g})".format(angle)]
872,874d809
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
890c825
<         return Instruction(CPhaseShift(angle), target=[control, target])
---
>         return Instruction(Gate.CPhaseShift(angle), target=[control, target])
905c840
<             angle=angle, qubit_count=None, ascii_symbols=["C", "PHASE00({:.3g})".format(angle)]
---
>             angle=angle, qubit_count=2, ascii_symbols=["C", "PHASE00({:.3g})".format(angle)]
915,917d849
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
933c865
<         return Instruction(CPhaseShift00(angle), target=[control, target])
---
>         return Instruction(Gate.CPhaseShift00(angle), target=[control, target])
948c880
<             angle=angle, qubit_count=None, ascii_symbols=["C", "PHASE01({:.3g})".format(angle)]
---
>             angle=angle, qubit_count=2, ascii_symbols=["C", "PHASE01({:.3g})".format(angle)]
958,960d889
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
976c905
<         return Instruction(CPhaseShift01(angle), target=[control, target])
---
>         return Instruction(Gate.CPhaseShift01(angle), target=[control, target])
991c920
<             angle=angle, qubit_count=None, ascii_symbols=["C", "PHASE10({:.3g})".format(angle)]
---
>             angle=angle, qubit_count=2, ascii_symbols=["C", "PHASE10({:.3g})".format(angle)]
1001,1003d929
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
1019c945
<         return Instruction(CPhaseShift10(angle), target=[control, target])
---
>         return Instruction(Gate.CPhaseShift10(angle), target=[control, target])
1029c955
<         super().__init__(qubit_count=None, ascii_symbols=["C", "Y"])
---
>         super().__init__(qubit_count=2, ascii_symbols=["C", "Y"])
1046,1048d971
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
1063c986
<         return Instruction(CY(), target=[control, target])
---
>         return Instruction(Gate.CY(), target=[control, target])
1073c996
<         super().__init__(qubit_count=None, ascii_symbols=["C", "Z"])
---
>         super().__init__(qubit_count=2, ascii_symbols=["C", "Z"])
1082,1084d1004
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
1099c1019
<         return Instruction(CZ(), target=[control, target])
---
>         return Instruction(Gate.CZ(), target=[control, target])
1117c1037
<             qubit_count=None,
---
>             qubit_count=2,
1138,1140d1057
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
1156c1073
<         return Instruction(XX(angle), target=[target1, target2])
---
>         return Instruction(Gate.XX(angle), target=[target1, target2])
1174c1091
<             qubit_count=None,
---
>             qubit_count=2,
1195,1197d1111
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
1213c1127
<         return Instruction(YY(angle), target=[target1, target2])
---
>         return Instruction(Gate.YY(angle), target=[target1, target2])
1231c1145
<             qubit_count=None,
---
>             qubit_count=2,
1250,1252d1163
<     def fixed_qubit_count() -> int:
<         return 2
<     @staticmethod
1268c1179
<         return Instruction(ZZ(angle), target=[target1, target2])
---
>         return Instruction(Gate.ZZ(angle), target=[target1, target2])
1281c1192
<         super().__init__(qubit_count=None, ascii_symbols=["C", "C", "X"])
---
>         super().__init__(qubit_count=3, ascii_symbols=["C", "C", "X"])
1302,1304d1212
<     def fixed_qubit_count() -> int:
<         return 3
<     @staticmethod
1320c1228
<         return Instruction(CCNot(), target=[control1, control2, target])
---
>         return Instruction(Gate.CCNot(), target=[control1, control2, target])
1330c1238
<         super().__init__(qubit_count=None, ascii_symbols=["C", "SWAP", "SWAP"])
---
>         super().__init__(qubit_count=3, ascii_symbols=["C", "SWAP", "SWAP"])
1351,1353d1258
<     def fixed_qubit_count() -> int:
<         return 3
<     @staticmethod
1369c1274
<         return Instruction(CSwap(), target=[control, target1, target2])
---
>         return Instruction(Gate.CSwap(), target=[control, target1, target2])
1443c1348
<         return Instruction(Unitary(matrix, display_name), target=targets)
---
>         return Instruction(Gate.Unitary(matrix, display_name), target=targets)
