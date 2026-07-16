---
alias: "script de Wolfram alpha"
date: 13-7-2026-(23:16)
---

# resumen

```
## Resumen de sesión — Script Wolfram Alpha

---

### 1. Completado

- Diseño y construcción completa de `main.py` para consultar WA Full API desde Shell Commands
- Preprocesador LaTeX→WA: `\lim`, `\frac`, `\int`, `\infty`, `\to`
- Traductor plaintext WA→LaTeX: símbolos, funciones, `\int`, `\sum`, `\prod`, `\lim`, subíndices/superíndices con `()→{}`
- Extracción dinámica de todos los pods (sin lista fija)
- Descarga de **todas** las gráficas PNG (múltiples subpods)
- Diccionario `DESCRIPTIVE_PHRASES` — frases descriptivas traducidas al español y extraídas fuera del `$$`
- Diccionario `POD_TITLES` — títulos de pods traducidos al español
- Cada línea del pod en su propio bloque `$$`
- Fracciones en texto plano (decisión tomada)
- Botón en Commander configurado
- Pruebas exitosas para cálculo 1: límites, derivadas, integrales, series, ecuaciones, matrices, conversiones, finanzas

---

### 2. Pendientes

**Títulos faltantes en `POD_TITLES`:**

- Faltan: `"Series expansion at x = ∞"`, `"Series representation"`, `"Integral representation"`, `"Parity"`, `"Polynomial discriminant"` y otros que aparezcan al probar
- Qué hacer: agregar al diccionario `POD_TITLES` en `main.py`
- Archivo: `E:\University_vault_2026\.obsidian\scripts\python\wolfram_query\src\main.py`
- Herramienta: `edit_file`

**Actualizar cabecera del script:**

- Reflejar estado real v15+ con todos los cambios de esta sesión
- Mismo archivo

**Documentar el script en el vault:**

- Crear nota de documentación del script
- Ruta sugerida: `E:\University_vault_2026\_app\shellcommands\`
- Leer antes: `E:\University_vault_2026\_app\_config\_claude-boot.md`

**Revisar `tsk_krajo.md`:**

- Marcar pendientes completados y actualizar decisiones
- Archivo: `E:\University_vault_2026\_tasks\tsk_krajo.md`

**Integrar en `Sin título 1.md`:**

- Marcar la idea de WA como implementada en la lista de ideas
- Archivo: `E:\University_vault_2026\Sin título 1.md`

---

**Detalle técnico crítico para la próxima sesión:**

- Backups disponibles: `mainv7.py.bk` hasta `mainv14.py.bk` en la misma carpeta `src/`
- El `\` en `re.sub` replacement: usar `r'\comando'` — NO `r'\\comando'` (produce doble backslash)
- `DESCRIPTIVE_PHRASES` itera sobre traducciones ya aplicadas — si se agrega una frase nueva, considerar que el texto ya fue procesado por `plaintext_to_latex` antes de llegar a `format_line`
- `expression_display` guarda el LaTeX original — `expression` es la versión convertida para WA
```



## Objetivo

15/july
> los pendientes estan el el codigo !!!! para WolframAlpha solo faltan detalles, se probo todo para lo que es calculo





claude debe integrar la lista de dops para lo cual aca esta la tabla y la lista en bruto, tambien estan los valores input con los que se extrajeron los dop con powershell

### Datos
Datos de el api de wolfram

| Name        | obsidian-vault             |
| ----------- | -------------------------- |
| App ID      | A3WL4X56LG                 |
| Description | personal vault integration |
| API         | Full Results API           |


$expr = "\lim_{x \to 0} \frac{\sin(x)}{x}"
$encoded = [System.Web.HttpUtility]::UrlEncode($expr)
$url = "https://api.wolframalpha.com/v2/query?input=$encoded&appid=A3WL4X56LG&output=json"
$r = Invoke-WebRequest -Uri $url -UseBasicParsing
($r.Content | ConvertFrom-Json).queryresult | Select-Object success, error

















---

## Pendientes

- [ ] Integrar los valores de los dops de la tabla en el script
- [ ] probar el script para los casos muestras
- [ ] documentar el script de wolfram
- [x] crear el boton de commander para el script en el meno de edicion
- [ ] si se puede que el script haga un fix de lo pegado desde wa la idea es que las fracciones se conviertan es eso  fracciones dentro de latex `\frac` por el momento se hace las correcciones a mano

> [!note]- Historial de pendientes
> **fecha** — 

---

## Completado

- [x] el script funcionabien para las pruebar resumidas
- [X] no es necesario que el script renombre a las imagenes que llegan de la pagina esto ya lo hace otro plugin

> [!note]- Historial de sesiones
> **fecha** — 

---

## Preguntas abiertas


---

## Herramientas / plugins

- shell command
- commander
---

## Archivos relacionados

### lista de dops (simplificada)

|                        title                        |                             id                              |
| :-------------------------------------------------: | :---------------------------------------------------------: |
|                       Result                        |       TotalValueStatisticsSharesPresent:FinancialData       |
|                    Company logo                     |                     Image:FinancialData                     |
|                Input interpretation                 |                            Input                            |
|                  Unit conversions                   |                       UnitConversion                        |
|                     Comparison                      |                      ComparisonAsArea                       |
|                   Interpretation                    |                       Interpretation                        |
|                Basic unit dimensions                |                     BasicUnitDimensions                     |
|              Corresponding quantities               |                    CorrespondingQuantity                    |
|                     Derivative                      |                            Input                            |
|                   Alternate form                    |                        AlternateForm                        |
|                        Roots                        |                      SymbolicSolution                       |
|            Properties as a real function            |                  PropertiesAsARealFunction                  |
|              Series expansion at x = 0              |                    SeriesExpansionAtx=0                     |
|                 Indefinite integral                 |                     IndefiniteIntegral                      |
|                    Global minima                    |                        GlobalMinimum                        |
|                    Global maxima                    |                        GlobalMaximum                        |
|                  Definite integral                  |                      DefiniteIntegral                       |
|            Definite integral mean square            |                 DefiniteIntegralMeanSquare                  |
|           Alternate form of the integral            |                 AlternateFormOfTheIntegral                  |
|            Expanded form of the integral            |                  ExpandedFormOfTheIntegral                  |
|      Series expansion of the integral at x = 0      |              SeriesExpansionOfTheIntegralAtx=0              |
|                  Input information                  |                            Input                            |
|                       Result                        |                           Result                            |
|                      Equation                       |                          Equation                           |
|           Present value vs. interest rate           |                 PresentValueVs.InterestRate                 |
|         Present value vs. interest periods          |               PresentValueVs.InterestPeriods                |
|           Present value vs. future value            |                 PresentValueVs.FutureValue                  |
|                 Comparison as speed                 |                      ComparisonAsSpeed                      |
|               Additional conversions                |                    AdditionalConversion                     |
|               Comparisons as distance               |                    ComparisonAsDistance                     |
|                   Interpretations                   |                       Interpretation                        |
|                Prime factorizations                 |                     PrimeFactorization                      |
|                       Results                       |                           Result                            |
|                        Plot                         |                            Plot                             |
|               Quotient and Remainder                |                    QuotientAndRemainder                     |
|                      Time span                      |                    DifferenceConversions                    |
|                       Result                        |                      Synonyms:WordData                      |
|                     Definitions                     |                     Definition:WordData                     |
|                   Current result                    |                           Result                            |
|                       History                       |              DistanceHistory:PlanetaryMoonData              |
|               Comparison as distance                |                    ComparisonAsDistance                     |
|                 Orbital properties                  |        BasicMoonOrbitalProperties:PlanetaryMoonData         |
|               Alternate complex forms               |                         PolarForms                          |
|            Position in the complex plane            |                  PositionInTheComplexPlane                  |
|                  Polar coordinates                  |                      PolarCoordinates                       |
|                 Minimal polynomial                  |                      MinimalPolynomial                      |
|                      ODE names                      |                          ODENames                           |
|                 ODE classification                  |                      ODEClassification                      |
|           Differential equation solutions           |                          Solution                           |
|  Differential equation series solution about x = 0  |         DifferentialEquationSeriesSolutionAboutx=0          |
|        Plots of sample individual solutions         |              PlotsOfSampleIndividualSolutions               |
|               Sample solution family                |                    SampleSolutionFamily                     |
|                 Possible Lagrangian                 |                     PossibleLagrangian                      |
|                         Sum                         |                            Input                            |
|                    Partial sums                     |                         PartialSums                         |
|                    Expanded form                    |                     MatrixExpandedForm                      |
|                     Dimensions                      |                         Dimensions                          |
|                     Matrix plot                     |                         MatrixPlot                          |
|                      Transpose                      |                       MatrixTranspose                       |
|                      Cofactors                      |                          Cofactors                          |
|                        Trace                        |                            Trace                            |
|                     Determinant                     |                         Determinant                         |
|              Characteristic polynomial              |                  CharacteristicPolynomial                   |
|                     Eigenvalues                     |                         Eigenvalues                         |
|                    Eigenvectors                     |                        Eigenvectors                         |
|                   Diagonalization                   |                       Diagonalization                       |
|                  Condition number                   |                       ConditionNumber                       |
|                Comparisons as length                |                     ComparisonAsLength                      |
|               Comparison as distance                |                    ComparisonAsDistance                     |
|                Comparison as height                 |                     ComparisonAsHeight                      |
|               Comparison as thickness               |                    ComparisonAsThickness                    |
|             Comparison as circumference             |                  ComparisonAsCircumference                  |
|           Electromagnetic frequency range           |                 FrequencyBands:QuantityData                 |
|                Visual representation                |                    VisualRepresentation                     |
|                Properties of circle                 |                         Properties                          |
|                      Root plot                      |                          RootPlot                           |
|                     Number line                     |                         NumberLine                          |
|                    Sum of roots                     |                         SumOfRoots                          |
|                  Product of roots                   |                       ProductOfRoots                        |
|                    Decimal form                     |                    DecimalApproximation                     |
|          Reference triangle for angle 30°           |                          Triangle                           |
|                 Continued fraction                  |                      ContinuedFraction                      |
|             Alternative representations             | AlternativeRepresentations:MathematicalFunctionIdentityData |
|                        Input                        |                            Input                            |
|                  Geometric figure                   |                GeometricFigure (ofBoundary)                 |
|          Alternate form assuming x is real          |                      RealAlternateForm                      |
|                        Roots                        |                            Root                             |
|                     Derivative                      |                         Derivative                          |
| Indefinite integral assuming all variables are real |        IndefiniteIntegralAssumingAllVariablesAreReal        |
|                   Global minimum                    |                        GlobalMinimum                        |
|                    Implicit plot                    |                      PlotOfSolutionSet                      |
|                        Limit                        |                            Limit                            |
|                        Plots                        |                            Plot                             |
|              Series expansion at x = 0              |                    SeriesExpansionAtX=x0                    |
|                      Divisors                       |                          Divisors                           |
|                                                     |                                                             |

### prompt de prueda

el prompt se lleva a powershell para que este entregue los dops

>se debe cambiar esta parte `input=prime+factorization+of+360&` para las pruebas, si hay mas de una entrada se usa & para concatenar las entradas

```
$url = "https://api.wolframalpha.com/v2/query?input=prime+factorization+of+360&appid=A3WL4X56LG&output=json"
$r = Invoke-WebRequest -Uri $url -UseBasicParsing
($r.Content | ConvertFrom-Json).queryresult.pods | Select-Object title, id
```

#### valores de prueba

>para el finanzas 1er intento no devolvió nada
>para español no devolvió nada

input=integrate+x*e^x+dx
input=solve+x^2-5x+6=0&expand+(x+2)^3&factor+x^3-8&
input=sin(30+degrees)&simplify+sin(x)^2+cos(x)^2&
input=area+of+circle+radius+5&volume+of+sphere+radius+3&
input=F=ma+solve+for+a&kinetic+energy+m=2kg+v=3m%2Fs&
input=mean+of+2%2C4%2C6%2C8%2C10&standard+deviation+2%2C4%2C6%2C8&
input=prime+factorization+of+360&is+97+prime&
input=100+miles+to+km&30+celsius+to+fahrenheit&
input={{1%2C2}%2C{3%2C4}}+inverse&determinant+{{1%2C2}%2C{3%2C4}}&
input=sum+n^2+from+1+to+10&fibonacci+sequence+first+10&geometric+series+ratio+1%2F2&
input=y''+2y'+y=0&dy%2Fdx=y&
input=(3%2B4i)*(1-2i)&modulus+of+3%2B4i&
input=union+{1%2C2%2C3}+{2%2C3%2C4}&intersection+{1%2C2%2C3}+{2%2C3%2C4}&
input=distance+from+earth+to+moon&mass+of+jupiter&
input=synonym+of+happy&etymology+of+science&
input=days+between+january+1+2000+and+today&what+day+is+july+4+2026&
input=simplify+(x^2-4)%2F(x-2)&complete+the+square+x^2+6x+5&partial+fractions+1%2F(x^2-1)&
input=GCD+48+18&LCM+12+15+20&sqrt(144)&2^10&
input=1+light+year+in+km&1+atmosphere+in+pascals&1+horsepower+in+watts&1+acre+in+square+meters&
input=speed+of+light+in+water&gravitational+force+m1=5kg+m2=10kg+r=2m&wavelength+of+440+Hz+sound&ohms+law+V=12+R=4&
input=future+value+1000+5+percent+10+years&NPV+rate=10%25+cashflows=100%2C200%2C300&simple+interest+principal=5000+rate=3%25+time=5+years&
input=integrar+x*e^x&
input=derivada+de+sin(x)&
input=mcm+12+15&
input=mcd+48+18&
#### valores que fallaron

xxxxinput=resolver+x^2-4=0&area+del+circulo+radio+5&factorial+de+6&distancia+de+la+tierra+a+la+luna&
xxxxxxinput=compound+interest+P=1000+r=5%25+t=10+years&mortgage+200000+30+years+6%25&
xxxxxinput=limite+de+sin(x)%2Fx+cuando+x+tiende+a+0&
xxxxinput=raices+de+x^2-5x+6&
xxxinput=volumen+de+esfera+radio+3&
xxxinput=simplificar+sin(x)^2%2Bcos(x)^2&

---

#### lista cruda

title                id
-----                --
Input interpretation Input
Result               TotalValueStatisticsSharesPresent:FinancialData
Company logo         Image:FinancialData

title                    id
-----                    --
Input interpretation     Input
Unit conversions         UnitConversion
Comparison               ComparisonAsArea
Interpretation           Interpretation
Basic unit dimensions    BasicUnitDimensions
Corresponding quantities CorrespondingQuantity

title                         id
-----                         --
Derivative                    Input
Plots                         Plot
Alternate form                AlternateForm
Roots                         SymbolicSolution
Properties as a real function PropertiesAsARealFunction
Series expansion at x = 0     SeriesExpansionAtx=0
Indefinite integral           IndefiniteIntegral
Global minima                 GlobalMinimum
Global maxima                 GlobalMaximum
Definite integral             DefiniteIntegral
Definite integral mean square DefiniteIntegralMeanSquare

title                                     id
-----                                     --
Indefinite integral                       IndefiniteIntegral
Plots                                     Plot
Alternate form of the integral            AlternateFormOfTheIntegral
Expanded form of the integral             ExpandedFormOfTheIntegral
Series expansion of the integral at x = 0 SeriesExpansionOfTheIntegralAtx=0
Definite integral                         DefiniteIntegral

title                              id
-----                              --
Input information                  Input
Result                             Result
Equation                           Equation
Present value vs. interest rate    PresentValueVs.InterestRate
Present value vs. interest periods PresentValueVs.InterestPeriods
Present value vs. future value     PresentValueVs.FutureValue

title                    id
-----                    --
Input interpretation     Input
Result                   Result
Unit conversions         UnitConversion
Comparison as speed      ComparisonAsSpeed
Corresponding quantities CorrespondingQuantity

title                    id
-----                    --
Input interpretation     Input
Result                   Result
Additional conversions   AdditionalConversion
Comparisons as distance  ComparisonAsDistance
Interpretations          Interpretation
Corresponding quantities CorrespondingQuantity

title                id
-----                --
Input                Input
Result               Result
Prime factorizations PrimeFactorization

title                  id
-----                  --
Input interpretation   Input
Results                Result
Plot                   Plot
Quotient and Remainder QuotientAndRemainder

title                id
-----                --
Input interpretation Input
Result               Result
Time span            DifferenceConversions

title                id
-----                --
Input interpretation Input
Result               Synonyms:WordData
Definitions          Definition:WordData

title                    id
-----                    --
Input interpretation     Input
Current result           Result
History                  DistanceHistory:PlanetaryMoonData
Unit conversions         UnitConversion
Comparison as distance   ComparisonAsDistance
Corresponding quantities CorrespondingQuantity
Orbital properties       BasicMoonOrbitalProperties:PlanetaryMoonData

title                id
-----                --
Input interpretation Input
Result               Result

title                         id
-----                         --
Input                         Input
Result                        Result
Alternate complex forms       PolarForms
Position in the complex plane PositionInTheComplexPlane
Polar coordinates             PolarCoordinates
Minimal polynomial            MinimalPolynomial

title                                             id
-----                                             --
Input                                             Input
ODE names                                         ODENames
ODE classification                                ODEClassification
Alternate form                                    AlternateForm
Differential equation solutions                   Solution
Differential equation series solution about x = 0 DifferentialEquationSeriesSolutionAboutx=0
Plots of sample individual solutions              PlotsOfSampleIndividualSolutions
Sample solution family                            SampleSolutionFamily
Possible Lagrangian                               PossibleLagrangian

title        id
-----        --
Sum          Input
Partial sums PartialSums

title                     id
-----                     --
Input                     Input
Result                    Result
Expanded form             MatrixExpandedForm
Dimensions                Dimensions
Matrix plot               MatrixPlot
Transpose                 MatrixTranspose
Cofactors                 Cofactors
Trace                     Trace
Determinant               Determinant
Characteristic polynomial CharacteristicPolynomial
Eigenvalues               Eigenvalues
Eigenvectors              Eigenvectors
Diagonalization           Diagonalization
Condition number          ConditionNumber

title                           id
-----                           --
Input interpretation            Input
Result                          Result
Additional conversions          AdditionalConversion
Comparisons as length           ComparisonAsLength
Comparison as distance          ComparisonAsDistance
Comparison as height            ComparisonAsHeight
Comparison as thickness         ComparisonAsThickness
Comparison as circumference     ComparisonAsCircumference
Electromagnetic frequency range FrequencyBands:QuantityData
Interpretations                 Interpretation
Corresponding quantities        CorrespondingQuantity

title                id
-----                --
Input interpretation Input
Result               Result
Divisors             Divisors

title  id
-----  --
Input  Input
Result Result

title                id
-----                --
Input interpretation Input
Result               Result

title                 id
-----                 --
Input interpretation  Input
Result                Result
Visual representation VisualRepresentation
Properties of circle  Properties

title                id
-----                --
Input interpretation Input
Results              Result
Root plot            RootPlot
Number line          NumberLine
Sum of roots         SumOfRoots
Product of roots     ProductOfRoots

title                            id
-----                            --
Input                            Input
Result                           Result
Decimal form                     DecimalApproximation
Reference triangle for angle 30° Triangle
Alternate form                   AlternateForm
Number line                      NumberLine
Continued fraction               ContinuedFraction
Alternative representations      AlternativeRepresentations:MathematicalFunctionIdentityData

title                                               id                            
-----                                               --
Input                                               Input
Geometric figure                                    GeometricFigure (ofBoundary)
Plots                                               Plot
Alternate form assuming x is real                   RealAlternateForm
Alternate form                                      AlternateForm
Roots                                               Root
Properties as a real function                       PropertiesAsARealFunction
Derivative                                          Derivative
Indefinite integral assuming all variables are real IndefiniteIntegralAssumingAllVariablesAreReal
Global minimum                                      GlobalMinimum

-----                                     --
Indefinite integral                       IndefiniteIntegral
Plots                                     Plot
Alternate form of the integral            AlternateFormOfTheIntegral
Expanded form of the integral             ExpandedFormOfTheIntegral
Series expansion of the integral at x = 0 SeriesExpansionOfTheIntegralAtx=0
Definite integral                         DefiniteIntegral

-----                --
Input interpretation Input
Result               Result
Implicit plot        PlotOfSolutionSet

-----                     --
Limit                     Limit
Plots                     Plot
Series expansion at x = 0 SeriesExpansionAtX=x0

-----                --
Input interpretation Input
Result               Result
Divisors             Divisors

---

## Decisiones

| Fecha | Decisión | Motivo |
| ----- | -------- | ------ |
|       |          |        |


---

%%
# galaxy-links
