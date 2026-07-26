from pathlib import Path
import re

SRC = Path('chatgpt-transfer/chap02_final_common_notation_v4.tex')
OUT = Path('chatgpt-transfer/chap02_final_readable_v5.tex')
REPORT = Path('chatgpt-transfer/第二章终稿可读公式版V5_验收报告.md')
CHECK = Path('chatgpt-transfer/check_chap02_readable_v5.tex')

text = SRC.read_text(encoding='utf-8')


def replace_equation(label: str, body: str) -> None:
    global text
    pattern = re.compile(
        r'\\begin\{equation\}.*?\\label\{' + re.escape(label) + r'\}.*?\\end\{equation\}',
        re.S,
    )
    replacement = '\\begin{equation}\n' + body.strip() + '\n\\label{' + label + '}\n\\end{equation}'
    text_new, count = pattern.subn(lambda _: replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f'Equation {label}: expected one match, found {count}')
    text = text_new


def replace_exact(old: str, new: str, name: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{name}: expected one match, found {count}')
    text = text.replace(old, new)


# 空间维数与坐标分量
replace_exact(
    '质量守恒方程为',
    '设空间维数为 $d$，$x_i$ 为第 $i$ 个空间坐标，流体速度的第 $i$ 个分量为 $v_{\\mathrm f,i}$。质量守恒方程为',
    'continuity introduction',
)

replace_equation(
    'eq:ch2_continuity',
    r'''
\sum_{i=1}^{d}
\frac{\partial v_{\mathrm f,i}}{\partial x_i}
=0.
''',
)

replace_equation(
    'eq:ch2_fluid_momentum',
    r'''
\rho
\left(
\frac{\partial v_{\mathrm f,i}}{\partial t}
+
\sum_{j=1}^{d}
v_{\mathrm f,j}
\frac{\partial v_{\mathrm f,i}}{\partial x_j}
\right)
=
-\frac{\partial p}{\partial x_i}
+
\sum_{j=1}^{d}
\frac{\partial}{\partial x_j}
\left[
\mu
\left(
\frac{\partial v_{\mathrm f,i}}{\partial x_j}
+
\frac{\partial v_{\mathrm f,j}}{\partial x_i}
\right)
\right]
+
\rho b_{\mathrm f,i}
+
F_{\gamma,i},
\qquad i=1,2,\ldots,d,
''',
)

replace_exact(
    '其中，$\\boldsymbol{b}_{\\mathrm f}$ 为单位质量体力，$\\boldsymbol{F}_{\\gamma}$ 为气液界面张力对应的体积力。流体 Cauchy 应力张量为',
    '其中，$b_{\\mathrm f,i}$ 为单位质量体力的第 $i$ 个分量，$F_{\\gamma,i}$ 为气液界面张力体积力的第 $i$ 个分量。流体 Cauchy 应力张量各分量为',
    'fluid force definitions',
)

replace_equation(
    'eq:ch2_fluid_stress',
    r'''
\sigma_{\mathrm f,ij}
=
-p\delta_{ij}
+
\mu
\left(
\frac{\partial v_{\mathrm f,i}}{\partial x_j}
+
\frac{\partial v_{\mathrm f,j}}{\partial x_i}
\right),
\qquad i,j=1,2,\ldots,d,
''',
)
replace_exact(
    '其中，$\\boldsymbol{I}$ 为单位张量。微通道问题不存在气液自由界面，因而 $\\boldsymbol{F}_{\\gamma}=\\boldsymbol{0}$。',
    '其中，$\\delta_{ij}$ 为 Kronecker 符号，当 $i=j$ 时取 $1$，当 $i\\ne j$ 时取 $0$。微通道问题不存在气液自由界面，因而 $F_{\\gamma,i}=0$。',
    'stress explanation',
)

# 相场公式展开
replace_equation(
    'eq:ch2_phase_free_energy',
    r'''
F_{\mathrm{CH}}(\varphi)
=
\int_{\Omega_{\mathrm f}}
\left[
\frac{\varepsilon_{\mathrm{int}}}{2}
\sum_{i=1}^{d}
\left(
\frac{\partial\varphi}{\partial x_i}
\right)^2
+
W_{\mathrm{dw}}
\left(\varphi^2-1\right)^2
\right]
\mathrm d\Omega,
''',
)
replace_exact(
    '其中，$\\varepsilon_{\\mathrm{int}}$ 为界面厚度参数，$W_{\\mathrm{dw}}$ 为双阱势垒系数。化学势 $G$ 为自由能对相场变量的变分导数',
    '其中，$\\varepsilon_{\\mathrm{int}}$ 为界面厚度参数，$W_{\\mathrm{dw}}$ 为双阱势垒系数。由该自由能得到的化学势为',
    'chemical potential prose',
)
replace_equation(
    'eq:ch2_phase_auxiliary',
    r'''
G
=
-\varepsilon_{\mathrm{int}}
\sum_{i=1}^{d}
\frac{\partial^2\varphi}{\partial x_i^2}
+
4W_{\mathrm{dw}}\varphi\left(\varphi^2-1\right).
''',
)
replace_equation(
    'eq:ch2_cahn_hilliard',
    r'''
\frac{\partial\varphi}{\partial t}
+
\sum_{i=1}^{d}
v_{\mathrm f,i}
\frac{\partial\varphi}{\partial x_i}
=
M
\sum_{i=1}^{d}
\frac{\partial^2G}{\partial x_i^2},
''',
)
replace_equation(
    'eq:ch2_phase_surface_force',
    r'''
F_{\gamma,i}
=
\frac{3\sqrt{2}}{4}
\frac{\gamma_{\mathrm{lg}}}{\varepsilon_{\mathrm{int}}}
\varphi\left(\varphi^2-1\right)
\frac{\partial\varphi}{\partial x_i},
\qquad i=1,2,\ldots,d.
''',
)
replace_equation(
    'eq:ch2_wetting_bc',
    r'''
\varepsilon_{\mathrm{int}}
\sum_{i=1}^{d}
n_{\Omega,i}
\frac{\partial\varphi}{\partial x_i}
+
\frac{\mathrm df_{\mathrm w}}{\mathrm d\varphi}
=0,
\qquad
\boldsymbol{x}\in\Gamma_{\mathrm w}.
''',
)
replace_equation(
    'eq:ch2_chemical_no_flux',
    r'''
\sum_{i=1}^{d}
n_{\Omega,i}
\frac{\partial G}{\partial x_i}
=0,
\qquad
\boldsymbol{x}\in\Gamma_{\mathrm w}.
''',
)
replace_equation(
    'eq:ch2_contact_angle_geometry',
    r'''
\cos\theta_{\mathrm e}
=
-\sum_{i=1}^{d}
n_{\mathrm{lg},i}n_{\mathrm w,i}.
''',
)

# 有限变形采用分量形式
replace_exact(
    '设固体参考构形为 $\\Omega_{\\mathrm s}^0$，材料点在参考构形和当前构形中的位置分别为 $\\boldsymbol{X}$ 和 $\\boldsymbol{x}$，$\\nabla_{\\!X}$ 表示相对于参考坐标 $\\boldsymbol{X}$ 的梯度算子。固体位移为',
    '设固体参考构形为 $\\Omega_{\\mathrm s}^0$，材料点在参考构形和当前构形中的位置分别为 $\\boldsymbol{X}$ 和 $\\boldsymbol{x}$，其第 $i$ 个坐标分量分别为 $X_i$ 和 $x_i$。固体位移为',
    'solid coordinate prose',
)
replace_equation(
    'eq:ch2_deformation_gradient',
    r'''
F_{ij}
=
\frac{\partial x_i}{\partial X_j}
=
\delta_{ij}
+
\frac{\partial u_{\mathrm s,i}}{\partial X_j},
\qquad
J=\det\left(F_{ij}\right).
''',
)
replace_equation(
    'eq:ch2_strain_tensors',
    r'''
C_{ij}
=
\sum_{k=1}^{d}F_{ki}F_{kj},
\qquad
E_{\mathrm{GL},ij}
=
\frac{1}{2}\left(C_{ij}-\delta_{ij}\right).
''',
)
replace_equation(
    'eq:ch2_invariants',
    r'''
I_1
=
\sum_{i=1}^{d}C_{ii},
\qquad
I_2
=
\frac{1}{2}
\left[
\left(\sum_{i=1}^{d}C_{ii}\right)^2
-
\sum_{i=1}^{d}\sum_{j=1}^{d}C_{ij}C_{ji}
\right],
\qquad
I_3
=
\det\left(C_{ij}\right)
=J^2.
''',
)
replace_equation(
    'eq:ch2_solid_momentum_reference',
    r'''
\rho_{\mathrm s}^0
\frac{\partial^2u_{\mathrm s,i}}{\partial t^2}
=
\sum_{j=1}^{d}
\frac{\partial P_{ij}}{\partial X_j}
+
\rho_{\mathrm s}^0b_{\mathrm s,i}^0,
\qquad i=1,2,\ldots,d.
''',
)
replace_exact(
    '其中，$\\rho_{\\mathrm s}^0$ 为参考构形密度，$\\boldsymbol{P}$ 为第一类 Piola--Kirchhoff 应力，$\\boldsymbol{b}_{\\mathrm s}^0$ 为单位质量体力。$\\boldsymbol{P}$ 与固体 Cauchy 应力 $\\boldsymbol{\\sigma}_{\\mathrm s}$ 之间满足',
    '其中，$\\rho_{\\mathrm s}^0$ 为参考构形密度，$P_{ij}$ 为第一类 Piola--Kirchhoff 应力分量，$b_{\\mathrm s,i}^0$ 为单位质量体力分量。$P_{ij}$ 与固体 Cauchy 应力分量 $\\sigma_{\\mathrm s,ij}$ 之间满足',
    'solid momentum definitions',
)
replace_equation(
    'eq:ch2_stress_transform',
    r'''
P_{ij}
=
J
\sum_{k=1}^{d}
\sigma_{\mathrm s,ik}
\left(F^{-1}\right)_{jk}.
''',
)

# Mooney--Rivlin 应力使用可直接计算的分量表达
replace_exact(
    '第二类 Piola--Kirchhoff 应力和弹性 Cauchy 应力分别为',
    '定义等容左 Cauchy--Green 变形张量分量为 $\\bar B_{ij}=J^{-2/3}\\sum_{k=1}^{d}F_{ik}F_{jk}$。弹性 Cauchy 应力分量为',
    'hyperelastic prose',
)
replace_equation(
    'eq:ch2_hyperelastic_stress',
    r'''
\begin{aligned}
\sigma_{\mathrm e,ij}
={}&
\kappa\left(J-1\right)\delta_{ij}
+
\frac{2C_{10}}{J}
\left(
\bar B_{ij}
-
\frac{\bar I_1}{3}\delta_{ij}
\right)
\\
&+
\frac{2C_{01}}{J}
\left[
\bar I_1\bar B_{ij}
-
\sum_{k=1}^{d}\bar B_{ik}\bar B_{kj}
-
\frac{2\bar I_2}{3}\delta_{ij}
\right].
\end{aligned}
''',
)

replace_equation(
    'eq:ch2_solid_rate',
    r'''
v_{\mathrm s,i}
=
\frac{\partial u_{\mathrm s,i}}{\partial t},
\qquad
D_{\mathrm s,ij}
=
\frac{1}{2}
\left(
\frac{\partial v_{\mathrm s,i}}{\partial x_j}
+
\frac{\partial v_{\mathrm s,j}}{\partial x_i}
\right).
''',
)
replace_exact(
    '近似不可压缩条件下，$\\operatorname{tr}\\boldsymbol{D}_{\\mathrm s}\\approx0$，黏性应力为偏应力。黏性应力和总 Cauchy 应力分别为',
    '近似不可压缩条件下，$\\sum_{i=1}^{d}D_{\\mathrm s,ii}\\approx0$，黏性应力主要表现为偏应力。黏性应力和总 Cauchy 应力分量分别为',
    'solid rate prose',
)
replace_equation(
    'eq:ch2_kelvin_voigt_3d',
    r'''
\sigma_{\mathrm v,ij}
=
\eta_{\mathrm s}D_{\mathrm s,ij},
\qquad
\sigma_{\mathrm s,ij}
=
\sigma_{\mathrm e,ij}
+
\sigma_{\mathrm v,ij}.
''',
)
replace_exact(
    '固体 Cauchy 应力的偏量和 von Mises 应力分别为',
    '对于三维应力状态，von Mises 应力由各应力分量计算为',
    'von Mises prose',
)
replace_equation(
    'eq:ch2_von_mises',
    r'''
\begin{aligned}
\sigma_{\mathrm{vM}}
=
\Bigg\{
&\frac{1}{2}
\left[
\left(\sigma_{xx}-\sigma_{yy}\right)^2
+
\left(\sigma_{yy}-\sigma_{zz}\right)^2
+
\left(\sigma_{zz}-\sigma_{xx}\right)^2
\right]
\\
&+
3\left(
\tau_{xy}^2
+
\tau_{yz}^2
+
\tau_{zx}^2
\right)
\Bigg\}^{1/2}.
\end{aligned}
''',
)
replace_exact(
    'von Mises 应力反映局部偏应力水平，弹性应变能表征细胞在变形过程中储存的整体弹性能。',
    '其中，$\\sigma_{xx}$、$\\sigma_{yy}$ 和 $\\sigma_{zz}$ 为正应力分量，$\\tau_{xy}$、$\\tau_{yz}$ 和 $\\tau_{zx}$ 为剪应力分量。von Mises 应力反映局部偏应力水平，弹性应变能表征细胞在变形过程中储存的整体弹性能。',
    'von Mises definitions',
)

# ALE 方程与界面条件采用分量形式
replace_equation(
    'eq:ch2_mesh_velocity',
    r'''
v_{\mathrm g,i}
=
\left.
\frac{\partial x_i}{\partial t}
\right|_{\boldsymbol{\chi}}
=
\frac{\partial u_{\mathrm g,i}}{\partial t},
\qquad i=1,2,\ldots,d.
''',
)
replace_equation(
    'eq:ch2_ale_derivative',
    r'''
\frac{\mathrm Dq}{\mathrm Dt}
=
\left.
\frac{\partial q}{\partial t}
\right|_{\boldsymbol{\chi}}
+
\sum_{j=1}^{d}
\left(v_{\mathrm f,j}-v_{\mathrm g,j}\right)
\frac{\partial q}{\partial x_j}.
''',
)
replace_equation(
    'eq:ch2_ale_ns',
    r'''
\begin{aligned}
\rho
\left[
\left.
\frac{\partial v_{\mathrm f,i}}{\partial t}
\right|_{\boldsymbol{\chi}}
+
\sum_{j=1}^{d}
\left(v_{\mathrm f,j}-v_{\mathrm g,j}\right)
\frac{\partial v_{\mathrm f,i}}{\partial x_j}
\right]
={}&
-\frac{\partial p}{\partial x_i}
\\
&+
\sum_{j=1}^{d}
\frac{\partial}{\partial x_j}
\left[
\mu
\left(
\frac{\partial v_{\mathrm f,i}}{\partial x_j}
+
\frac{\partial v_{\mathrm f,j}}{\partial x_i}
\right)
\right]
+
\rho b_{\mathrm f,i}
+
F_{\gamma,i},
\\
&\hspace{7cm}i=1,2,\ldots,d.
\end{aligned}
''',
)
replace_equation(
    'eq:ch2_ale_cahn_hilliard',
    r'''
\left.
\frac{\partial\varphi}{\partial t}
\right|_{\boldsymbol{\chi}}
+
\sum_{j=1}^{d}
\left(v_{\mathrm f,j}-v_{\mathrm g,j}\right)
\frac{\partial\varphi}{\partial x_j}
=
M
\sum_{j=1}^{d}
\frac{\partial^2G}{\partial x_j^2}.
''',
)
replace_equation(
    'eq:ch2_fsi_kinematic',
    r'''
v_{\mathrm f,i}
=
v_{\mathrm s,i}
=
v_{\mathrm g,i},
\qquad
i=1,2,\ldots,d,
\qquad
\boldsymbol{x}\in\Gamma_{\mathrm{fs}}.
''',
)
replace_equation(
    'eq:ch2_fsi_dynamic',
    r'''
\sum_{j=1}^{d}
\left(
\sigma_{\mathrm f,ij}n_{\mathrm f,j}
+
\sigma_{\mathrm s,ij}n_{\mathrm s,j}
\right)
=0,
\qquad
i=1,2,\ldots,d,
\qquad
\boldsymbol{x}\in\Gamma_{\mathrm{fs}}.
''',
)

# 弱形式全部展开为分量求和
replace_equation(
    'eq:ch2_weak_fluid_momentum',
    r'''
\begin{aligned}
&\int_{\Omega_{\mathrm f}}
\rho
\sum_{i=1}^{d}
w_{\mathrm f,i}
\left[
\left.
\frac{\partial v_{\mathrm f,i}}{\partial t}
\right|_{\boldsymbol{\chi}}
+
\sum_{j=1}^{d}
\left(v_{\mathrm f,j}-v_{\mathrm g,j}\right)
\frac{\partial v_{\mathrm f,i}}{\partial x_j}
\right]
\mathrm d\Omega
\\
&\quad+
\int_{\Omega_{\mathrm f}}
\mu
\sum_{i=1}^{d}\sum_{j=1}^{d}
\frac{\partial w_{\mathrm f,i}}{\partial x_j}
\left(
\frac{\partial v_{\mathrm f,i}}{\partial x_j}
+
\frac{\partial v_{\mathrm f,j}}{\partial x_i}
\right)
\mathrm d\Omega
-
\int_{\Omega_{\mathrm f}}
p
\sum_{i=1}^{d}
\frac{\partial w_{\mathrm f,i}}{\partial x_i}
\mathrm d\Omega
\\
&=
\int_{\Omega_{\mathrm f}}
\sum_{i=1}^{d}
w_{\mathrm f,i}
\left(
\rho b_{\mathrm f,i}
+
F_{\gamma,i}
\right)
\mathrm d\Omega
+
\int_{\Gamma_{\mathrm t}^{\mathrm f}}
\sum_{i=1}^{d}
w_{\mathrm f,i}\bar t_{\mathrm f,i}
\mathrm d\Gamma.
\end{aligned}
''',
)
replace_equation(
    'eq:ch2_weak_continuity',
    r'''
\int_{\Omega_{\mathrm f}}
w_p
\sum_{i=1}^{d}
\frac{\partial v_{\mathrm f,i}}{\partial x_i}
\mathrm d\Omega
=0.
''',
)
replace_equation(
    'eq:ch2_weak_phase_transport',
    r'''
\begin{aligned}
&\int_{\Omega_{\mathrm f}}
w_{\varphi}
\left[
\left.
\frac{\partial\varphi}{\partial t}
\right|_{\boldsymbol{\chi}}
+
\sum_{j=1}^{d}
\left(v_{\mathrm f,j}-v_{\mathrm g,j}\right)
\frac{\partial\varphi}{\partial x_j}
\right]
\mathrm d\Omega
\\
&\qquad+
\int_{\Omega_{\mathrm f}}
M
\sum_{j=1}^{d}
\frac{\partial w_{\varphi}}{\partial x_j}
\frac{\partial G}{\partial x_j}
\mathrm d\Omega
=0.
\end{aligned}
''',
)
replace_exact(
    '对式~\\eqref{eq:ch2_phase_auxiliary}分部积分，并在非润湿边界取 $\\boldsymbol{n}_{\\Omega}\\cdot\\nabla\\varphi=0$，可得',
    '对式~\\eqref{eq:ch2_phase_auxiliary}分部积分，并在非润湿边界取 $\\sum_{j=1}^{d}n_{\\Omega,j}\\partial\\varphi/\\partial x_j=0$，可得',
    'phase weak prose',
)
replace_equation(
    'eq:ch2_weak_phase_auxiliary',
    r'''
\begin{aligned}
&\int_{\Omega_{\mathrm f}}
w_GG\,\mathrm d\Omega
-
\int_{\Omega_{\mathrm f}}
\varepsilon_{\mathrm{int}}
\sum_{j=1}^{d}
\frac{\partial w_G}{\partial x_j}
\frac{\partial\varphi}{\partial x_j}
\mathrm d\Omega
\\
&\qquad-
\int_{\Omega_{\mathrm f}}
4W_{\mathrm{dw}}
w_G\varphi\left(\varphi^2-1\right)
\mathrm d\Omega
+
\int_{\Gamma_{\mathrm w}}
\varepsilon_{\mathrm{int}}w_G
\sum_{j=1}^{d}
n_{\Omega,j}
\frac{\partial\varphi}{\partial x_j}
\mathrm d\Gamma
=0,
\end{aligned}
''',
)
replace_equation(
    'eq:ch2_weak_wetting_term',
    r'''
\int_{\Gamma_{\mathrm w}}
\varepsilon_{\mathrm{int}}w_G
\sum_{j=1}^{d}
n_{\Omega,j}
\frac{\partial\varphi}{\partial x_j}
\mathrm d\Gamma
=
-
\int_{\Gamma_{\mathrm w}}
w_G
\frac{\mathrm df_{\mathrm w}}{\mathrm d\varphi}
\mathrm d\Gamma.
''',
)
replace_equation(
    'eq:ch2_weak_solid',
    r'''
\begin{aligned}
&\int_{\Omega_{\mathrm s}^0}
\rho_{\mathrm s}^0
\sum_{i=1}^{d}
w_{\mathrm s,i}
\frac{\partial^2u_{\mathrm s,i}}{\partial t^2}
\mathrm d\Omega_0
+
\int_{\Omega_{\mathrm s}^0}
\sum_{i=1}^{d}\sum_{j=1}^{d}
\frac{\partial w_{\mathrm s,i}}{\partial X_j}
P_{ij}
\mathrm d\Omega_0
\\
&=
\int_{\Omega_{\mathrm s}^0}
\rho_{\mathrm s}^0
\sum_{i=1}^{d}
w_{\mathrm s,i}b_{\mathrm s,i}^0
\mathrm d\Omega_0
+
\int_{\Gamma_{\mathrm t}^{\mathrm s,0}}
\sum_{i=1}^{d}
w_{\mathrm s,i}\bar T_{\mathrm s,i}
\mathrm d\Gamma_0.
\end{aligned}
''',
)
replace_exact(
    '其中，$\\Gamma_{\\mathrm t}^{\\mathrm s,0}$ 为参考构形中的给定牵引边界，$\\bar{\\boldsymbol{T}}_{\\mathrm s}$ 为名义牵引。',
    '其中，$\\Gamma_{\\mathrm t}^{\\mathrm s,0}$ 为参考构形中的给定牵引边界，$\\bar T_{\\mathrm s,i}$ 为名义牵引的第 $i$ 个分量。',
    'solid traction definition',
)

# Newton 迭代改为分量形式
replace_equation(
    'eq:ch2_discrete_residual',
    r'''
R_a\left(U_1,U_2,\ldots,U_{N_{\mathrm d}}\right)
=0,
\qquad a=1,2,\ldots,N_{\mathrm d},
''',
)
replace_exact(
    '其中，$\\boldsymbol{U}$ 为全部待求自由度，$\\boldsymbol{R}$ 为离散残差向量。采用 Newton 迭代求解非线性方程组\\cite{ypma1995historical}，其形式为',
    '其中，$U_a$ 为第 $a$ 个待求自由度，$R_a$ 为对应离散残差，$N_{\\mathrm d}$ 为总自由度数。采用 Newton 迭代求解非线性方程组\\cite{ypma1995historical}，其形式为',
    'residual prose',
)
replace_equation(
    'eq:ch2_newton_iteration',
    r'''
\sum_{b=1}^{N_{\mathrm d}}
K_{ab}^{(m)}
\Delta U_b^{(m)}
=
-R_a\left(U_1^{(m)},U_2^{(m)},\ldots,U_{N_{\mathrm d}}^{(m)}\right),
\qquad
U_a^{(m+1)}
=
U_a^{(m)}
+
\Delta U_a^{(m)}.
''',
)
replace_exact(
    '其中，$\\boldsymbol{K}^{(m)}=\\partial\\boldsymbol{R}/\\partial\\boldsymbol{U}$ 为切线矩阵，$\\Delta\\boldsymbol{U}^{(m)}$ 为增量向量，$m$ 为非线性迭代次数。',
    '其中，$K_{ab}^{(m)}=\\partial R_a/\\partial U_b$ 为切线矩阵第 $a$ 行第 $b$ 列的元素，$\\Delta U_b^{(m)}$ 为第 $b$ 个自由度的增量，$m$ 为非线性迭代次数。',
    'Newton definitions',
)

# 几何与网络公式中的范数和矩阵运算展开
replace_equation(
    'eq:ch2_polygon_perimeter',
    r'''
L_{\Gamma}
=
\sum_{i=1}^{N_{\mathrm c}}
\sqrt{
\left(x_{i+1}-x_i\right)^2
+
\left(y_{i+1}-y_i\right)^2
}.
''',
)
replace_equation(
    'eq:ch2_fully_connected_layer',
    r'''
a_j^{(k)}
=
f^{(k)}
\left(
\sum_{i=1}^{N_{k-1}}
W_{ji}^{(k)}a_i^{(k-1)}
+
b_j^{(k)}
\right),
\qquad j=1,2,\ldots,N_k.
''',
)
replace_exact(
    '其中，$\\boldsymbol{W}^{(k)}$ 和 $\\boldsymbol{b}^{(k)}$ 分别为第 $k$ 层的权重矩阵和偏置向量，$f^{(k)}$ 为激活函数。',
    '其中，$N_{k-1}$ 和 $N_k$ 分别为第 $k-1$ 层和第 $k$ 层的神经元数，$W_{ji}^{(k)}$ 为连接两层神经元的权重，$b_j^{(k)}$ 为偏置，$f^{(k)}$ 为激活函数。',
    'FNN definitions',
)
replace_equation(
    'eq:ch2_mse',
    r'''
\mathcal{L}_{\mathrm{MSE}}
=
\frac{1}{N_{\mathrm{tr}}N_{\mathrm o}}
\sum_{s=1}^{N_{\mathrm{tr}}}
\sum_{j=1}^{N_{\mathrm o}}
\left(
\widehat y_{s,j}-y_{s,j}
\right)^2,
''',
)
replace_exact(
    '预测误差由损失函数衡量。本文采用的通用均方误差（Mean Squared Error，MSE）为',
    '预测误差由损失函数衡量。设网络输出变量数为 $N_{\\mathrm o}$，通用均方误差（Mean Squared Error，MSE）为',
    'MSE prose',
)
replace_equation(
    'eq:ch2_parameter_update',
    r'''
\theta_j^{(r+1)}
=
\theta_j^{(r)}
-
\alpha_r
\frac{\partial\mathcal L}{\partial\theta_j}
\bigg|_{\boldsymbol{\theta}=\boldsymbol{\theta}^{(r)}},
''',
)
replace_exact(
    '其中，$r$ 为迭代次数，$\\alpha_r$ 为第 $r$ 次迭代的学习率。',
    '其中，$r$ 为迭代次数，$\\alpha_r$ 为第 $r$ 次迭代的学习率，$\\theta_j$ 为第 $j$ 个可训练参数。',
    'parameter update definition',
)

# 统一相应文字中的矢量符号
text = text.replace('$\\bar{\\boldsymbol{t}}_{\\mathrm f}$ 为边界牵引', '$\\bar t_{\\mathrm f,i}$ 为边界牵引的第 $i$ 个分量')

# 静态检查
labels = re.findall(r'\\label\{([^}]+)\}', text)
refs = re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}', text)
cites = [k.strip() for group in re.findall(r'\\cite\{([^}]+)\}', text) for k in group.split(',')]
duplicates = sorted({x for x in labels if labels.count(x) > 1})
missing_refs = sorted(set(refs) - set(labels))

forbidden = {
    'tensor_double_contraction': r'\\boldsymbol\{[^}]+\}\s*:',
    'trace_operator': r'\\operatorname\{tr\}',
    'vector_two_norm': r'\\left\\\|',
    'variational_derivative': r'\\frac\{\\delta',
    'tensor_energy_derivative': r'\\frac\{\\partial W_\{\\mathrm\{MR\}\}\}\{\\partial\\boldsymbol',
}
forbidden_hits = {name: len(re.findall(pattern, text)) for name, pattern in forbidden.items()}

# 基础环境闭合检查
environments = ['equation', 'aligned', 'align', 'section', 'subsection']
env_counts = {}
for env in environments[:3]:
    env_counts[env] = (text.count('\\begin{' + env + '}'), text.count('\\end{' + env + '}'))

if duplicates:
    raise RuntimeError(f'Duplicate labels: {duplicates}')
if missing_refs:
    raise RuntimeError(f'Missing refs: {missing_refs}')
if any(forbidden_hits.values()):
    raise RuntimeError(f'Forbidden abstract operators remain: {forbidden_hits}')
if any(a != b for a, b in env_counts.values()):
    raise RuntimeError(f'Unclosed environments: {env_counts}')

OUT.write_text(text, encoding='utf-8')

report = f'''# 第二章终稿可读公式版 V5 验收报告

## 本轮修改范围

本轮以公式可读性为主要目标。变量名称基本沿用上一版，重点展开弱形式、应力、张量不变量、有限元非线性方程、轮廓周长和神经网络损失中的抽象运算。张量双点积、迹运算、二范数、变分导数和对应的矩阵乘法均改为分量求和或直接可计算形式。

## 静态检查

- 标签数量：{len(labels)}
- 重复标签：{len(duplicates)}
- 交叉引用数量：{len(refs)}
- 缺失交叉引用：{len(missing_refs)}
- 不同文献键数量：{len(set(cites))}
- 张量双点积残留：{forbidden_hits['tensor_double_contraction']}
- `tr` 运算残留：{forbidden_hits['trace_operator']}
- 二范数残留：{forbidden_hits['vector_two_norm']}
- 变分导数残留：{forbidden_hits['variational_derivative']}
- 应变能对张量的形式导数残留：{forbidden_hits['tensor_energy_derivative']}
- equation 环境：{env_counts['equation'][0]} 对
- aligned 环境：{env_counts['aligned'][0]} 对
- align 环境：{env_counts['align'][0]} 对

## 冻结边界

静态检查通过只说明 LaTeX 源码结构、公式标签和指定抽象运算检查合格。是否可正式冻结，还需以独立 XeLaTeX 与 BibTeX 编译结果、版面溢出检查和 PDF 页面检查为准。
'''
REPORT.write_text(report, encoding='utf-8')

CHECK.write_text(r'''\documentclass[12pt,a4paper]{ctexrep}
\usepackage{amsmath,amssymb,bm,booktabs,array}
\usepackage[numbers,sort&compress]{natbib}
\setlength{\textwidth}{15.5cm}
\setlength{\textheight}{23cm}
\begin{document}
\input{chap02_final_readable_v5.tex}
\bibliographystyle{unsrt}
\bibliography{refs_ch2_final_locked}
\end{document}
''', encoding='utf-8')

print(f'Generated {OUT}')
print(f'Generated {REPORT}')
print(f'Generated {CHECK}')
