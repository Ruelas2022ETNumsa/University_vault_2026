7.3 MULTIPERIOD OPERATIONS
In writing the SIC control sequence in Chapter 6, we assumed that all
transfer operations could be completed in one clock period. However,
there are many casesin which transters or logicoperations may require
more than one clock period. Memory access is one such situation. Be
cause of cost, main random access memory is often realized in technol-
ogy that is slower than register memory. Since the majority of transfers
involve registers, the clock rate is set accordingly, and any slower trans-
fers will require multiple clock periods.
As discussed in Chapter 3, many different technologies may be con-
sidered for implementing random access memories. These many types
of memories differ greatly in signal and timing requirements. In terms
of the control sequence steps required to control them, the majority of
memory systems can be grouped into three categories, which we shall
reterto as clocked. slow synchronous,and asynchronous., The clocked
memory is the simplest to handle, being logically equivalent to an array
of clocked registers. Normally realized in TTL or ECL technology, such
a memory is fully compatible in speed with the control unit. The general
model for a clocked memory is shown in FEig313, There are address
lines, separate input and output lines for data, and a single control line,
write enable,whichis equivalent to the clock line tor a register
To apply such a memory in SIC, the address lines would be driven
by the output of MA, the data in lines would be driven by the output of
MD, and the data out lines will drive the input of MD. For a read
operation, if an address is applied to the address lines by loading MA
in one clock period, then the data is available to be transferred to MD
at the end of the next clock period. Thus a pair of statements such as
2. MA PC
3. MD BUSFN(M; DCD(MA)
is sutficient to specify a read operation. For a write operation, if the
address and data to be written are supplied in one clock period, applying
the next clock pulse to the write enable line will complete the operation.
Thus two statements of the form
4. MD-AC; MA-IRs:17
22.
M
* DCD(MA) -MD
are sufficient to specify a write operation.
Such clocked memories are generally limited to rather small size by
cost factors. For larger memories, the slow synchronous or asynchronous

memories are usually preferable in terms of cost. The slow synchronous
memory type, of which the static MOS memory is the most common
example, is not clocked by short pulses in the manner of registers but
instead requires level control signals extending for one or more clock
periods. We considersuch memories to be synchronous in the sense,
that the timing of control signals is entirely controlled by the central
controlunt. Such units also commonly share a single bus for both input
and output of data. Figure 7.6 shows the basic model for a typical mem-
ory of this type, consisting of 1024 words of 18 bits each. Addresses are
provided over 10-bit ADDLINE; data are transferred over the 18-bit
MEMBUS. There are two control lines, read and enable. The line read
must be at the 1-level for a read operation, at the 0-level for a write. Fo
a read operation, the addressmust be stable on ADDLINE for a mini
mum of one clockperiodbeforeenablegoes to 1 and must remain stable
as long as enableis up. The output data will be available two clock
periods ater enable goes up and will remain available as long as enahle
IS up. The line read must be stable for the same period as the address.
ror a write operation, the data to be written must be stable for the same
period as the address, for one period betore enable goes up and tor two
periods after.
Because of the bus and separate control lines, the memory must be
eclared as a separate module and the communication lines must be
added to the declarations for SIC.
OUTPUTS: ADDLINE[10]; read; enable
COMBUS: MEMBUS [18]
ese lines would similarly be declared as INPUTS and COMBUS in
descrption of the memory module. We shall assumethat ADDLINE
will be driven by the low-order 10 bits of MA, as specified by the state-
ment

ADDLINE = MA3:12
after END SEQUENCE.
With this model and connections as indicated, a typicalreadsequence
would appear as follows.
2. MA-PC
3. read = 1
4.
enable = 1; read = 1|
5 enable = 1; read = 1; MD -MEMBUS
The clock pulse at the end of step 2 establishes the address in MA and
thus on ADDLINE. At the beginning of step 3, read is set to 1. At the
start of step 4, after a delay of l period, enable is set to 1, and read
continues at 1. This condition is held through step 5, until the data word
is transferred into MD from MEMBUS by the clock pulse at the end of
step 5, two clock periods after enable was set to 1.
A typical/write sequence would appear as follows.
4. MA-PC;MD-AC
5. MEMBUS = MD; read = 0
6. MEMBUS = MD; enable = l; read =0
7. MEMBUS = MD; enable = l; read = 0
The most common forms of asynchronous memoryin use at this time
corememory and dynamic MOS memory.These types of memories
will usually have their own timing and control circuitry, and are best
treated as separate asynchronous modules. Such a module will probably
have its own intrinsic address and data registers, which cannot be
treated as CPU registers. Let us now consider how a typical asynchro-
nous memory organization could be incorporated in the SIC control
sequence.
The organization of the memory module is shown in Fig. 7.7. The
memory module includes the memory itself (8192 x 18); address and
data registers (MAR and MDR); address and data input lines
(MEMADDR[13) and DATAIN[18]; data output lines DATAOUT[18);
control input lines (read and write) and a control output line, busy. The
control lines are at the 0-level when the memory is not in use. To initiate
à memory operation, the CPU will set read or write to logic 1 and gate
appropriate information onto the address and data lines. The memory
will respond by gating MEMADDR into MAR and, for a write operation,
DATAIN into MDR, and will then raisebusy to the Llevel. At this point

the CPU may lower read or uwrite and clear the address and data lines.
When the memory cycle is complete and, for a read operation, the re
quested word is on the DATAOUT lines, busy will return to the 0-1evel.
It is important to note that the CPU "sees the memory only in terms
of the communications lines. The existence of the MAR and MDR reg
isters will not be indicated in the CPU sequence in any way. We have
mentioned them solely for the sake of clarity in the discussion of mem-
ory operation.
The first modification required in the SIC control sequence is to add
the memory communications lines to the INPUT and OUTPUT and
BUS declarations.
INPUTS: busy; DATAOUT[18];
OUTPUTS:
read; write; MEMADDR[13]; DATAIN[I18]
BUS: MEMADBUS[13]
The register MA is no longer required in the CPU. In the CPU se-
guence, MA appears only as a destination for transfers from PC or IR.
It never serves as a source, nor are its contents ever manipulated. Steps
could be saved by eliminating transfers to MA and declaringa
MEMADBUS. The outputs of either PC or IR may be connected to
IEMADBUS, and the MEMADDR lines to memory are permanently
connected to MEMADBUS by the statement
MEMADDR = MEMADBUS
TOllowing END SEQUENCE. If MA remains in the CPU, we would
write
MEMADDR = MA
following END SEQUENCE.

Although we could dispense with the MA register, it is desirable to
retain the MD register. In the implementation of the ISZ command the
contents of MD must be manipulated, independent of any memory op-
erations. This cannot be done in MDR, since that register cannot be
controlled by the CPU. We shall also find a separate MD register useful
in IO operations. On the other hand, there is no longer any need to
route all memory operations through MD. Instead, DATAOUT can be
an input to the OBUS, and DATAIN an output of the OBUS.
The use of an asynchronous memory will also necessitate changes in
the body of the control sequence. Assumingno MA, let us considerthe
modifications necessary to the SIC control sequence steps that fetch a
new instruction. The original steps (from Chapter 6) and the new steps
are shown side-by-side for ease of comparison.
2. MA -PC
3. MEMADBUS
= PC read
= 1,
»SYN(busy)/(2)
4. MD BUSFN(M; DCD(MA)) 3. null
SYN(busy)/(3)
4.
NO DELAY
5. IR -
MD
OBUS
= 0, DATAOUT;
IR-OBUS 1:18
(New sequence)
(Old sequence)
Since we no longer have an MA register, the new step 2 connects the
output of PC to MEMADDR. Step 2 also sets read to 1 and waits for
busy to go up, acknowledging the read request. Step 3 then waits for
busy to go down, signaling completion of the memory cycle; step 4 then
transfers the word from DATAOUT to IR, via the OBUS. Note that there
is no need to pass the instruction word through MD, so we take advan-
tage of the connection of DATAOUT to the OBUS to move the instruc-
tion directly to IR.
The control unit and timing diagram for these new steps are shown
in Fig. 7.8. The logical I on read is provided by connecting CSL2 to the
read line through an OR gate. The other inputs to the OR gate will be
control levels from other read steps in the sequence. Control holds at
step 2 until busy goes up and then holds at step 3 until busy goes doWn.
Note that CSLA overlaps CSL3, a situation characteristic of NO DELAY
steps. The interaction in this sequence, raising read and then waiting
for busy to go up as an acknowledgment, and then waiting for busy to
go down, as an indication that the operation is complete, is an example
of a handshaking interchange, This is a standard technique of commu-
ications between systems, and it will be more fully discussed in Chap-
ters 9 and 10.

The reader may recall from Chapter 3 that in a read operation in a
core memory, the data word read is available about halfway through the
memory cycle, since the word has to be rewritten after being read. Be-
cause of this, a core memory will often have another output line, data-
ready, indicating when the requested word is available on the DA-
AOUT ines. Obviously, the operation of the computer can be speeded
up it the CPU picks up the word as soon as this signal appears, rather
an wait for the end of the complete memory cycle. However, doing so
w create certain complications. Since the sequence proceeds without
waiting for the end of the memory cycle, it is possible that the sequence
dy Teach another step requiring a memory operation betore the pre-
us cycle is complete. Similar considerations apply to write oper
S, In which it would be possible for the CPU to proceed to other
nemory operations as soon as busy goes up, acknowledging receipt
ne data to be stored. Modifi cation of the SIC control sequence for
memory operations and consideration of the problems of overlap-
*
operations and memory operations will be left as exercises

for the reader. Throughout the remainder of the book, the clocked mem-
ory will be assumed except where otherwise specifically indicated.
Multiperiod delays will also be required if there are logic operations
that need more than one clock period to complete. One place where this
situation may occur is in the adder. For reasons of delay in combina-
tional logic, as will be discussed later in this chapter, the time from the
gating of the operands to the adder inputs to the appearance of the
correct sum at the output may be much longer than the time required
tor a simple register transfer. In the case of SIC, this would require that
the outputs of AC and MD be held on the ABUS and BBUS for several
clock periods.
In Chapter 6 an alternative control sequence was presented, which
branched to separate steps for each of the AND, TAD, and LAC oper-
ations. This approach can more easily handle unequal timing of opera-
tions than can the conditional transfer approach. The corresponding
steps 17 to 20 with busing connections given explicitly are
17. NO DELAY
(IR,A IR,), (IR, AIR,), (IR,AIR,)/(18, 19, 20)
18. BBUS = MD; OBUS = 0, BBUS; AC-OBUS1:18
(24)
19. ABUS = AC; BBUS = MD; OBUS = 0, (ABUS A BBUS);
AC-OBUS 1:18
(24)
20. ABUS = AC; BBUS = MD
OBUS ADD{ABUS; BBUS);Y, AC-OBUs
(24)
Let us also assume an adder that requires three clock periods to develop
a sum. Since we have separated control for the ADD step, only step 20
need be modified. To allow for the extra delay, we replace the above
step 20 with the following three steps.
20-1.
ABUS = AC; BBUS = MD
20-2.
ABUS = AC; BBUS = MD
20-3. ABUS = AC; BBUS
= MD;
OBUS
= ADD(ABUS; BBUS); f, AC -OBUS
(24)
The corresponding control circuit is shown in Fig. 7.9. Note that the
outputs of the three step-20 flip-flops are OR'ed to hold AC and MD on
the ABUS and BBUS for the three clock periods required to allow for
adder propagation.

The above approach is satisfactory for short delays but would be very
expensive for long delays. For long delays it will generally be preferable
to count the required number of clock periods or use a one-shot to gen-
erate an arbitrary delay.
As an example of the tormer approach, let us consider the same se-
qmence as above, but let us now assume that eight clock periods are
required tor adder propagation. We shall provide a 3-bit counter,
ADDCNT, to count the eight periods of delay. ADDCNT will be reset
to zero at step 16, at the same time MD is loaded with the memory
output. The original step 20 will be replaced by the following.
20.
ABUS = AC; BBUS = MD; ADDCNT-INC (ADDNT)
OBUS
= ADD(ABUS; BBUS)
, AC) * (AWADDCNT)-OBUS
(MADDCNT), (IADDCNT)Y(20, 24)
Step 20 provides a waiting loop that holds at this step, incrementing
ADDCNT each clock time, until the count reaches 111. Since the branch
is on the value of ADDCNT prior to incrementing, a count of 111 indi-
cates that the sequence has held at this step for eight clock periods. At
this time the transfer is completed and control branches to step 24.
As an example of the use of a one-shot, let us consider another adder
requiring 10 clock periods for propagation delay. We shall declare
a
synchronized one-shot, addsyn.
ONE-SHOT: addsyn(10)
This one-shot will be triggered at step 17, by adding the transfer state
ment
17. addsyn*(IR, A IR,) 1
NO DELAY
Step 20 will now be
18. ABUS
= AC; BBUS = MD;
OBUS = ADD(ABUS; BBUS)
, AC)
* addsyn -OBUS
(addsyn, addsyn)/(20, 24)
Thus the operation will be the same as in the counter realization except
that step 20 will wait for the end of the 10-period delay generated by
addsyn.
We have seen three methods of providing multiperiod delays. The
Cnoice among these methods will be based primarily on cost. For delays
TOur periods or less, the first approach, adding extra delay tHip-tlop

will generally be preferable. For longer delays, the one-shot approach
be noted that one-shots are prone to erroneous triggering due to noise.
and some designers feel they should be avoided at all costs.