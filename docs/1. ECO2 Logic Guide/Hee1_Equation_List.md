---
title: 시작하기
slug: /ECO2_사용자_도움말/시작하기
---

# 시작하기

본 매뉴얼은 ECO2 제로에너지인증 평가프로그램의 기능과 구조를 체계적으로 이해하고 활용할 수 있도록 지원하기 위해 작성되었습니다. 프로그램의 주요 기능을 분석하고, 기능 간 연계 구조와 실행 흐름을 정리하였으며, 주요 로직은 플로우차트 등 시각 자료로 구성하여 이해도를 높였습니다.

건축, 냉·난방 설비, 조명, 환기, 신재생에너지 등 각 분야별 로직을 설명하고, 실제 적용 사례를 함께 수록함으로써 실무적 활용성을 강화하였습니다. 본 매뉴얼은 발주처와의 협의를 통해 초안을 검토하고 피드백을 반영하여 작성되었으며, 사용자 중심의 명확한 정보 전달을 목표로 합니다.

ECO2 프로그램의 활용에 본 매뉴얼이 실질적인 도움이 되기를 기대합니다.



# 수식 정리  


## 🔹존의 난방부하


\[ 
Q_{h,b.mth} = d_{op} \left( Q_{sink,op} - \eta_{op} Q_{source,op} \right) + d_{we} \left( Q_{sink,we} - \eta_{we} Q_{source,we} \right) \tag{2-6}
\] 

$$
Q_{h,b.mth} = d_{op} \left( Q_{sink,op} - \eta_{op} Q_{source,op} \right) + d_{we} \left( Q_{sink,we} - \eta_{we} Q_{source,we} \right) \tag{2-6}
$$

$$
Q_{h,b,i} = Q_{sink,i} - \eta_i Q_{source,i} \tag{2-1}
$$

$$
Q_{source} = Q_S + Q_T + Q_V + Q_{I,source} \tag{2-16}
$$

$$
Q_{sink} = Q_T + Q_V + Q_{I,sink} + Q_S \tag{2-11}
$$

$$
\eta = \frac{1 - \gamma^a}{1 - \gamma^{a+1}}, \quad \gamma \ne 1 \tag{2-23}
$$

$$
\eta = \frac{a}{a+1}, \quad \gamma = 1 \tag{2-24}
$$

$$
\gamma = \frac{Q_{source}}{Q_{sink}} \tag{2-21}
$$

$$
H_{T,D} = \sum (U_j A_j) + \Delta U_{WB} \sum A_j \tag{2-44}
$$

$$
H_{T,D} = \sum (U_j A_j) + \sum (l_j \Psi_j) \tag{2-45}
$$

$$
H_{T,iu} = \sum (U_j A_j) \tag{2-48}
$$

$$
H_{T,iz} = \sum (U_j A_j) \tag{2-52}
$$

$$
H_{T,s} \quad (\text{DIN EN ISO 13370 } L_s)
$$

$$
1 - (\eta \gamma) < 0.01 \rightarrow \eta = \frac{1}{\gamma}, \quad (Q_{h,b} = 0) \tag{2-137}
$$

$$
(1 - \eta) \gamma < 0.01 \rightarrow \eta = 1, \quad (Q_{c,b} = 0) \tag{2-138}
$$

$$
\dot{V}_{mech} \geq \frac{\dot{Q}_{C,max}}{c_{p,a} \rho_a (\vartheta_i - \vartheta_{mech})} \rightarrow \eta = 1 \tag{2-139}
$$

$$
a = a_0 + \frac{\tau}{\tau_0}, \quad a_0 = 1, \quad \tau_0 = 16h \tag{2-25}
$$

$$
\tau = \frac{C_{wirk}}{H} = \frac{C_{wirk}}{\sum_j H_{T,j} + \sum_k H_{V,k} + H_{V,mech,\vartheta}} \tag{2-22, 129}
$$

$$
H_{V,inf} = n_{inf} \, V \, c_{p,a} \, \rho_a \tag{2-58}
$$

$$
H_{V,mech} = n_{mech} \, V \, c_{p,a} \, \rho_a \tag{2-83}
$$

$$
H_{V,ue} = n_{ue} \, V_u \, c_{p,a} \, \rho_a \tag{2-94}
$$

$$
H_{V,z} = \dot{V}_{z,d} \, c_{p,a} \, \rho_a \tag{2-99}
$$

$$
C_{wirk} = 50 \, \mathrm{Wh}/(\mathrm{m}^2 \cdot \mathrm{K}) \, A_B \tag{2-126}
$$

$$
C_{wirk} = 90 \, \mathrm{Wh}/(\mathrm{m}^2 \cdot \mathrm{K}) \, A_B \tag{2-127}
$$

$$
C_{wirk} = 130 \, \mathrm{Wh}/(\mathrm{m}^2 \cdot \mathrm{K}) \, A_B \tag{2-128}
$$

$$
H_{V,mech,\vartheta} = H_{V,mech} \cdot \frac{\vartheta_{i,h.soll} - \vartheta_{V,mech}}{6K} \tag{2-130}
$$



## 🔹존의 냉방부하


$$
Q_{c,b.mth} = d_{op} (1 - \eta_{op}) Q_{source,op} + d_{we} (1 - \eta_{we}) Q_{source,we} \tag{2-7}
$$

$$
Q_{h,c} = (1 - \eta) Q_{source} \tag{2-1}
$$

$$
Q_{source} = Q_S + Q_T + Q_V + Q_{I,source} \tag{2-16}
$$

$$
\eta = \frac{1 - \gamma^a}{1 - \gamma^{a+1}}, \quad \gamma \ne 1 \tag{2-23}
$$

$$
\eta = \frac{a}{a+1}, \quad \gamma = 1 \tag{2-24}
$$

$$
\gamma = \frac{Q_{source}}{Q_{sink}} \tag{2-21}
$$

$$
H_{T,D} = \sum (U_j A_j) + \Delta U_{WB} \sum A_j \tag{2-44}
$$

$$
H_{T,iu} = \sum (U_j A_j) \tag{2-48}
$$

$$
H_{T,iz} = \sum (U_j A_j) \tag{2-52}
$$

$$
H_{T,s} \quad (\text{DIN EN ISO 13370 } L_s)
$$

$$
Q_{sink} = Q_T + Q_V + Q_{I,sink} + Q_S \tag{2-11}
$$

$$
1 - (\eta \gamma) < 0.01 \rightarrow \eta = \frac{1}{\gamma}, \quad (Q_{h,b} = 0) \tag{2-137}
$$

$$
(1 - \eta) \gamma < 0.01 \rightarrow \eta = 1, \quad (Q_{c,b} = 0) \tag{2-138}
$$

$$
\dot{V}_{mech} \geq \frac{\dot{Q}_{C,max}}{c_{p,a} \rho_a (\vartheta_i - \vartheta_{mech})} \rightarrow \eta = 1 \tag{2-139}
$$

$$
a = a_0 + \frac{\tau}{\tau_0}, \quad a_0 = 1, \quad \tau_0 = 16h \tag{2-25}
$$

$$
\tau = \frac{C_{wirk}}{H} = \frac{C_{wirk}}{\sum_j H_{T,j} + \sum_k H_{V,k} + H_{V,mech,\vartheta}} \tag{2-22, 129}
$$

$$
H_{V,inf} = n_{inf} \, V \, c_{p,a} \, \rho_a \tag{2-58}
$$

$$
H_{V,mech} = n_{mech} \, V \, c_{p,a} \, \rho_a \tag{2-83}
$$

$$
H_{V,ue} = n_{ue} \, V_u \, c_{p,a} \, \rho_a \tag{2-94}
$$

$$
H_{V,z} = \dot{V}_{z,d} \, c_{p,a} \, \rho_a \tag{2-99}
$$

$$
C_{wirk} = 50 \, \mathrm{Wh}/(\mathrm{m}^2 \cdot \mathrm{K}) \, A_B \tag{2-126}
$$

$$
C_{wirk} = 90 \, \mathrm{Wh}/(\mathrm{m}^2 \cdot \mathrm{K}) \, A_B \tag{2-127}
$$

$$
C_{wirk} = 130 \, \mathrm{Wh}/(\mathrm{m}^2 \cdot \mathrm{K}) \, A_B \tag{2-128}
$$

$$
H_{V,mech,\vartheta} = H_{V,mech} \cdot \frac{\vartheta_{i,h.soll} - \vartheta_{V,mech}}{6K} \tag{2-130}
$$



## 🔹열손실


$$
Q_{sink} = Q_T + Q_V + Q_{I,sink} + Q_S \tag{2-11}
$$

$$
Q_T = \sum_j H_{T,j} \cdot (\vartheta_i - \vartheta_j)t, \quad \vartheta_i > \vartheta_j \tag{2-12}
$$

$$
Q_{T,e} = H_{T,D} (\vartheta_i - \vartheta_e)t, \quad \vartheta_i > \vartheta_e \tag{2-42}
$$

$$
Q_{T,u} = H_{T,iu} (\vartheta_i - \vartheta_u)t, \quad \vartheta_i > \vartheta_u \tag{2-46}
$$

$$
Q_{T,z} = H_{T,iz} (\vartheta_i - \vartheta_z)t, \quad \vartheta_i > \vartheta_z \tag{2-50}
$$

$$
Q_{T,s} = H_{T,s} (\vartheta_i - \vartheta_s)t, \quad \vartheta_i > \vartheta_s \tag{2-53}
$$

$$
H_{T,D} = \sum (U_j A_j) + \Delta U_{WB} \sum A_j \tag{2-44}
$$

$$
H_{T,iu} = \sum (U_j A_j) \tag{2-48}
$$

$$
H_{T,iz} = \sum (U_j A_j) \tag{2-52}
$$

$$
H_{T,s} \quad (\text{DIN EN ISO 13370 } L_s)
$$

$$
\Delta U_{WB} :
\begin{cases}
0.1 & \text{외단열 (external insulation)} \\
0.15 & \text{내단열 (internal insulation)}
\end{cases}
\quad \text{(참조: 식 2-24)}
$$

$$
\tau = \frac{C_{wirk}}{H} = \frac{C_{wirk}}{\sum_j H_{T,j} + \sum_k H_{V,k} + H_{V,mech,\vartheta}} \tag{2-22, 129}
$$

$$
Q_V = \sum_k H_{V,k} (\vartheta_i - \vartheta_k)t, \quad \vartheta_i > \vartheta_k \tag{2-13}
$$

$$
Q_{V,inf} = H_{V,inf} (\vartheta_i - \vartheta_e)t, \quad \vartheta_i > \vartheta_e \tag{2-56}
$$

$$
Q_{V,win} = H_{V,win} (\vartheta_i - \vartheta_e)t, \quad \vartheta_i > \vartheta_e \tag{2-64}
$$

$$
Q_{V,mech} = H_{V,mech} (\vartheta_i - \vartheta_{V,mech})t, \quad \vartheta_i > \vartheta_{V,mech} \tag{2-81}
$$

$$
Q_{V,z} = H_{V,z} (\vartheta_j - \vartheta_z)t, \quad \vartheta_j > \vartheta_z \tag{2-97}
$$

$$
\vartheta_i = \vartheta_{i,h} \ \text{oder} \ \vartheta_{i,c} \quad \text{(난방 또는 냉방 분석 – 실내온도)}
$$

$$
\vartheta_{i,h} = \vartheta_{i,h.soll} \tag{2-26} \quad \text{기본 21°C}
$$

$$
\vartheta_{i,h} = \max \left( \vartheta_{i,h.soll} - f_{NA,d} (\vartheta_{i,h.soll} - \vartheta_e), \ \vartheta_{i,h.soll} - \Delta \vartheta_{i,NA,d} \cdot \frac{t_{NA,d}}{24h} \right) \tag{2-27} \quad \text{야간감소}
$$

$$
\vartheta_{i,h} = \max \left( \vartheta_{i,h.soll} - f_{ue} (\vartheta_{i,h.soll} - \vartheta_e), \ \vartheta_{i,h.soll} - \Delta \vartheta_{i,NA,d} \right) \tag{2-30} \quad \text{주말감소}
$$

$$
\vartheta_{i,h} = \vartheta_{i,h.soll} - f_{tb} (\vartheta_{i,h.soll} - \vartheta_e) \tag{2-33} \quad \text{공간적 제한}
$$

$$
\vartheta_{i,h} = \vartheta_{i,NA} - f_{tb} (\vartheta_{i,NA} - \vartheta_e) \tag{2-35} \quad \text{공간적 시간적 제한}
$$

$$
\vartheta_{i,c} = \vartheta_{i,c.soll} - 2K \tag{2-36} \quad \text{예: } 24^\circ \text{C} - 2K = 22^\circ \text{C}
$$

---

$$
\vartheta_{V,mech} = \vartheta_e \tag{2-90} \quad \text{공조처리 없는 경우}
$$

$$
\vartheta_{V,mech} = \vartheta_e + \eta_{V,mech} \cdot (\vartheta_i - \vartheta_e) \tag{2-91} \quad \text{비제어식 열교환}
$$

$$
\vartheta_{V,mech} = \vartheta_{V,mech,RLT} \tag{2-92} \quad \text{공조처리된 급기온도 (도표 3-3, 3-4, 7-5)}
$$

$$
t_{NA} = 24h - t_{h,op.d}, \quad \Delta \vartheta_{i,NA} = 4K \quad \text{(용도별 조건)}
$$

$$
f_{we} = 0.2 \left( 1 - 0.4 \cdot \frac{\tau}{250h} \right) \tag{2-31} \quad \text{난방감소}
$$

$$
f_{NA} = 0.13 \cdot \frac{t_{NA}}{24h} \left( - \frac{\tau}{250h} \right) \tag{2-28}
$$

$$
f_{we} = 0.3 \left( 1 - 0.2 \cdot \frac{\tau}{250h} \right) \tag{2-32} \quad \text{난방정지}
$$

$$
f_{NA} = 0.26 \cdot \frac{t_{NA}}{24h} \left( - \frac{\tau}{250h} \right) \tag{2-29}
$$

$$
f_{tb} = 0.8 \left[ 1 - \exp \left( - \frac{\dot{Q}_{h,\mathrm{max}}}{A_B \cdot 35 \, \mathrm{W/m^2}} \right) \right] a_{tb}^2 \tag{2-34}
$$

$$
a_{tb} = \frac{A_{beheizt}}{A_B}
$$

$$
Q_{I,sink} = Q_{I,sink,c} + Q_{I,sink,fac} \tag{2-15}
$$

$$
Q_{I,sink,c} = Q_{I,vh} + Q_{I,c} \tag{2-125}
$$

$$
Q_{I,sink,fac} = q_{I,sink,fac} \cdot A_B \tag{2-120}
$$

$$
Q_{I,sink,goods} = c m (\vartheta_{out} - \vartheta_{in}) t, \quad \vartheta_{in} < \vartheta_{out} \tag{2-122}
$$

$$
H_{V,inf} = n_{inf} \, V \, c_{p,a} \, \rho_a \tag{2-58}
$$

$$
H_{V,mech} = n_{mech} \, V \, c_{p,a} \, \rho_a \tag{2-83}
$$

$$
H_{V,ue} = n_{ue} \, V_u \, c_{p,a} \, \rho_a \tag{2-94}
$$

$$
H_{V,z} = \dot{V}_{z,d} \, c_{p,a} \, \rho_a \tag{2-99}
$$

$$
Q_S = Q_{S,op} = R_{se} \, UA \left( F_f h_r \Delta \vartheta_{er} - \alpha I_S \right)t, \quad \alpha I_S < F_f h_r \Delta \vartheta_{er} \tag{2-111}
$$

$$
F_f = 1 \quad \text{(45°까지)}
$$

$$
F_f = 0.5 \quad \text{(45°~90°)}
$$

$$
h_r = 5 \varepsilon \quad \text{(모를 경우 } \varepsilon = 0.9\text{)}
$$

$$
\Delta \vartheta_{er} = 10K \quad \text{(천공온도차)}
$$

$$
c_{p,a} \, \rho_a = 0.34 \, \mathrm{Wh}/(\mathrm{m}^3 \cdot \mathrm{K})
$$



## 🔹열획득


$$
Q_{source} = Q_S + Q_T + Q_V + Q_{I,source} \tag{2-16}
$$

$$
Q_S = \sum Q_{S,tr} + \sum Q_{S,op} \tag{2-17}
$$

$$
Q_{S,tr} = F_F A \, g_{eff} \, I_S \, t \tag{2-105}
$$

- \( F_F \): 창틀비율 \( (= 0.7) \)
- \( A \): 개구부 면적

$$
g_{eff} = F_S F_W F_V g_\perp \tag{2-106} \quad \text{비차양}
$$

$$
g_{eff} = F_S F_W F_V g_{tot} \tag{2-107} \quad \text{차양}
$$

- 자동차양 (2-108) 일단 유보:

$$
g_{eff} = F_W F_V \cdot \min \left( a_{g,tot}(1 - a) g_\perp,\; F_S g_\perp \right)
$$


$$
F_S = \min(F_h, F_o, F_f) \tag{2-109}
$$

- \( F_W = 0.9 \)
- \( F_V = 0.9 \)
- 투과율 (차양 유무에 따른 값): 도표 (2-5) 참고
- 부록 A 도표에서 관련 계수 확인 가능

$$
Q_{S,op} = R_{se} \, UA \left( \alpha I_S - F_f h_r \Delta \vartheta_{er} \right)t, \quad \text{if } \alpha I_S > F_f h_r \Delta \vartheta_{er} \tag{2-112}
$$

- \( F_f = 1 \quad \text{(45°까지)} \)
- \( F_f = 0.5 \quad \text{(45°~90°)} \)
- \( h_r = 5 \varepsilon \quad \text{(모를 경우 } \varepsilon = 0.9\text{)} \)
- \( \Delta \vartheta_{er} = 10K \quad \text{(천공온도차)} \)

$$
Q_T = \sum_j H_{T,j} \cdot (\vartheta_j - \vartheta_i)t, \quad \vartheta_i < \vartheta_j \tag{2-18}
$$

$$
Q_{T,e} = H_{T,D} (\vartheta_e - \vartheta_i)t, \quad \vartheta_i < \vartheta_e \tag{2-43}
$$

$$
Q_{T,u} = H_{T,iu} (\vartheta_u - \vartheta_i)t, \quad \vartheta_i < \vartheta_u \tag{2-47}
$$

$$
Q_{T,z} = H_{T,iz} (\vartheta_z - \vartheta_i)t, \quad \vartheta_i < \vartheta_z \tag{2-51}
$$

$$
Q_{T,s} = H_{T,s} (\vartheta_e - \vartheta_i)t, \quad \vartheta_i < \vartheta_e \tag{2-54}
$$

$$
H_{T,D} = \sum (U_j A_j) + \Delta U_{WB} \sum A_j \tag{2-44}
$$

$$
H_{T,iu} = \sum (U_j A_j) \tag{2-48}
$$

$$
H_{T,iz} = \sum (U_j A_j) \tag{2-52}
$$

$$
H_{T,s} \quad (\text{DIN EN ISO 13370 } L_s)
$$

$$
\Delta U_{WB} =
\begin{cases}
0.10 & \text{외단열 (external insulation)} \\
0.15 & \text{내단열 (internal insulation)}
\end{cases}
\quad \text{(참조: 식 2-24)}
$$

$$
Q_V = \sum_k H_{V,k} (\vartheta_k - \vartheta_i)t, \quad \vartheta_i < \vartheta_k \tag{2-19}
$$

$$
Q_{V,inf} = H_{V,inf} (\vartheta_e - \vartheta_i)t, \quad \vartheta_i < \vartheta_e \tag{2-57}
$$

$$
Q_{V,win} = H_{V,win} (\vartheta_e - \vartheta_i)t, \quad \vartheta_i < \vartheta_e \tag{2-65}
$$

$$
Q_{V,mech} = H_{V,mech} (\vartheta_{V,mech} - \vartheta_i)t, \quad \vartheta_i < \vartheta_{V,mech} \tag{2-82}
$$

$$
Q_{V,z} = H_{V,z} (\vartheta_z - \vartheta_i)t, \quad \vartheta_i < \vartheta_z \tag{2-98}
$$

- 이하 열손실과 같음

$$
Q_{I,source} = Q_{I,source,p} + Q_{I,source,L} + Q_{I,source,fac} + Q_{I,source,h} \tag{2-20}
$$

$$
Q_{I,source,p} = q_{I,p} \cdot A_B \tag{2-118}
$$

$$
Q_{I,source,fac} = q_{I,fac} \cdot A_B \tag{2-119}
$$

$$
Q_{i,L} = \mu_L \cdot Q_{i,L,elektr} \tag{2-123}
$$

$$
Q_{I,source,h} = Q_{I,w} + Q_{I,h} + Q_{I,vh} + Q_{I,ch} \tag{2-124}
$$

- \( q_{I,p} \): 도표 2-A.4 (사람에 의한 내부발생열)
- \( q_{I,fac} \): 도표 2-A.4 (설비기기에 의한 내부발생열)
- \( Q_{i,L,elektr} \): 조명에 의한 전기적 소비량



## 🔹환기에 의한 열손실계수


$$
H_{V,inf} = n_{inf} V c_{p,a} \rho_a \tag{2-58}
$$

$$
H_{V,mech} = n_{mech} V c_{p,a} \rho_a \tag{2-83}
$$

$$
H_{V,ue} = n_{ue} V_u c_{p,a} \rho_a \tag{2-94}
$$

$$
H_{V,z} = \dot{V}_{z,d} c_{p,a} \rho_a \tag{2-99}
$$

환기기기 없는 경우:
$$
n_{inf} = n_{50} \cdot e_{wind} \tag{2-59}
$$

환기기기 있는 경우:
$$
n_{inf} = n_{50} \cdot e_{wind} \left( 1 + f_{V,mech} \cdot \frac{t_{V,mech}}{24h} \right) \tag{2-60}
$$

- \( n_{50} \): 도표 2-4 참고 (50 Pa에서의 침기 회수)
- \( e_{wind} = 0.07 \): 바람 보정계수

$$
f_{V,mech} = 0,\quad n_{ZUL} = n_{ABL} \tag{2-61}
$$

$$
f_{V,mech} = \frac{1}{1 + \dfrac{f_{wind}}{e_{wind}} \left( \dfrac{n_{ZUL} - n_{ABL}}{n_{50}} \right)^2} - 1, \quad n_{ZUL} > n_{ABL} \tag{2-62}
$$

$$
f_{V,mech} = 1 - \frac{1}{1 + \dfrac{f_{wind}}{e_{wind}} \left( \dfrac{n_{ZUL} - n_{ABL}}{n_{50}} \right)^2}, \quad n_{ABL} > n_{ZUL} \tag{2-63}
$$

- \( n_{mech,ABL} = n_{mech,ZUL} \): 모를 경우  
- \( n_{mech,ABL} = n_{nutz} \): 순수배기

$$
n_{nutz} = \frac{\dot{V}_A \cdot A_B}{V} \tag{2-80}
$$

- \( \dot{V}_A \): 최소 외기량 (용도 프로필 기준)

$$
n_{mech} = \max(n_{mech,ZUL},\; n_{nutz}) \cdot \frac{t_{V,mech}}{24h} \tag{2-84}
$$

$$
n_{mech} = n_{mech,ZUL} = 0\; h^{-1},\quad \text{순수배기} \tag{2-88}
$$

- \( t_{V,mech} \): 기계 환기 작동 시간 (용도 프로필 기준)

$$
n_{mech,ZUL} = \frac{\dot{V}_{mech,b}}{V} \tag{2-87}
$$

$$
n_{mech,ABL} = \frac{\dot{V}_{ABL}}{V} \tag{2-89}
$$

$$
n_{ue} = 0.6\; h^{-1} \quad \text{(표준값)} \tag{2-96}
$$

$$
\dot{V}_{z,d} = \dot{V}_z \cdot \frac{t_{V,mech}}{24h} \tag{2-100}
$$

- \( t_{V,mech} \): 기계환기 가동 시간 (용도 프로필 기준)

$$
\dot{V}_z = n_{z,ZUL} \cdot V \tag{2-101}
$$

$$
\dot{V}_z = n_{z,ABL} \cdot V \tag{2-103}
$$

$$
n_{z,ZUL} = n_{mech,ABL} - n_{mech,ZUL} \tag{2-102}
$$

$$
n_{z,ABL} = \frac{\dot{V}_z}{V_i} = \left( n_{mech,ABL,j} - n_{mech,ZUL,j} \right) \cdot \frac{V_j}{V_i} \tag{2-104}
$$

- \( i \): 건물존  
- \( j \): 이웃존

$$
\dot{V}_{mech,b} = \frac{\dot{Q}_{c,\text{max}}}{c_{p,a} \rho_a (\vartheta_i - \vartheta_{V,mech})} \quad \text{냉방정풍량기기} \tag{2-86}
$$

- \( \dot{V}_{ABL} \): 계획 값 (부록 E 참고)

---



## 🔹공조처리


$$
Q_{V,i,m} = q_{i,m} \cdot \dot{V}_{mech,m} \quad (3\text{-}36) = Q_{vi,b} \quad \text{(7-2, 7-8, 7-14)} \quad \text{[Wh]}
$$

$$
q_{i,m} = q_{i,12h,m} \cdot \frac{t_{V,mech,m}}{12} \cdot f_{h,i} \cdot \frac{d_{V,mech,m}}{d_{max,m}} \tag{3-28}
$$

$$
q_{H,12h,m} = q_{H,18^\circ C,12h,m} + g_{H,o,m} (\vartheta_{HC} - 18^\circ C), \quad 18^\circ C < \vartheta_{HC} \leq 22^\circ C \tag{3-23}
$$

$$
q_{H,12h,m} = q_{H,18^\circ C,12h,m} + g_{H,u,m} (\vartheta_{HC} - 18^\circ C), \quad 14^\circ C < \vartheta_{HC} \leq 18^\circ C \tag{3-24}
$$

$$
q_{C,12h,m} = q_{C,18^\circ C,12h,m} - g_{C,o,m} (\vartheta_{HC} - 18^\circ C), \quad 18^\circ C < \vartheta_{HC} \leq 22^\circ C \tag{3-25}
$$

$$
q_{C,12h,m} = q_{C,18^\circ C,12h,m} - g_{C,u,m} (\vartheta_{HC} - 18^\circ C), \quad 14^\circ C < \vartheta_{HC} \leq 18^\circ C \tag{3-26}
$$

$$
q_{St,12h,m} = q_{St,18^\circ C,12h,m} \tag{3-27}
$$

$$
f_{h,i} \quad \text{그림 (3-4)}
$$

도표 A.1~A.13

$$
q_{i,18^\circ C,12h,m}
$$

$$
g_{H,o,m}, \quad g_{H,u,m}
$$

$$
g_{C,o,m}, \quad g_{C,u,m}
$$

$$
\vartheta_{HC,m} = \vartheta_{V,mech,m} - \frac{Q_{V,E,ZUL,m}}{t_{V,mech,m} \, d_{V,mech,m} \, c_{p,L} \rho_L \, \dot{V}_{mech,m}} + 1.4K \tag{3-22}
$$

$$
Q_{V,E,ZUL,m} = P_{V,ZUL,m} \, t_{V,mech,m} \, d_{V,mech,m} \tag{3-10} \quad \text{정풍량 [Wh]}
$$

$$
Q_{V,E,ZUL,m} = \sum_j t_{V,mech,j,m} \, P_{V,ZUL,j} \tag{3-14} \quad \text{시간, 용도 변풍량 [Wh]}
$$

$$
Q_{V,E,ZUL,m} = \frac{\Delta p^{*}_{ZUL} \, f_{p,ZUL}}{\eta_{ZUL}} \sum_m \dot{V}_{ZUL} + 
\frac{\Delta p^{*}_{ZUL} (1 - f_{p,ZUL})}{\eta_{ZUL} \, \dot{V}^{*2}_{ZUL}} \sum_m \dot{V}^3_{ZUL} 
\tag{3-16} \quad \text{변풍량 냉방부하}
$$

$$
P_{V,ZUL,m} = \frac{\dot{V}_{ZUL} \, \Delta p^{*}_{ZUL}}{\eta_{ZUL} \cdot 3600} \tag{3-7} 
\quad \text{정풍량 [W]}
$$

$$
P_{V,ZUL} = 
\left( 
\frac{\dot{V}_{ZUL} \, \Delta p^{*}_{ZUL} \, f_{p,ZUL}}{\eta_{ZUL}} + 
\frac{\dot{V}_{ZUL}^3 \, \Delta p^{*}_{ZUL} (1 - f_{p,ZUL})}{\eta_{ZUL} \, \dot{V}_{ZUL}^{*2}} 
\right) \cdot \frac{1}{3600}
\tag{3-11}
\quad \text{변풍량 [W]}
$$

$$
\eta_{ZUL} = \eta_{tot} \quad \text{(도표 7-3)}
$$

$$
\Delta p^{*}_{ZUL} = \Delta p_{tot} \quad \text{(도표 7-3)}
$$

$$
\dot{V}_{ZUL} = \dot{V}_{ABL} = \dot{V}_{mech,m} \tag{3-18}
$$

$$
f_p = \frac{\Delta p_{konst}}{\Delta p^*} = 0.4 \quad \text{(3-13, 7-1)}
$$

$$
\dot{V}_{mech,b,m} = \dot{V}_{mech,m} = \dot{V}^* \quad \text{(3-1) 정풍량}
$$

$$
\dot{V}_{mech,m} = \frac{\sum_j V_j \cdot t_{V,mech,j,m}}{t_{V,mech,m} \cdot d_{V,mech,m}} \quad \text{(3-2) 시간, 용도}
$$

$$
\dot{V}_{mech,m} = \dot{V}_{mech,b,m} + \frac{1000 \cdot Q_{c,b}}{t_{V,mech,m} \cdot d_{V,mech,m} \cdot c_{p,L} \rho_L (\vartheta_{i,c,m} - \vartheta_{V,mech,m})} \tag{3-4}
$$

$$
\sum_m \dot{V} = t_{V,mech,m} \cdot d_{V,mech,m} \cdot \dot{V}_{mech,b,m} + \frac{1000 \cdot Q_{c,b}}{c_{p,L} \rho_L (\vartheta_{i,c,m} - \vartheta_{V,mech,m})} \tag{3-5}
$$

$$
\vartheta_{i,c} = \vartheta_{i,c,soll} - 2K \tag{2-36}
$$

$$
Q_{c,b} \tag{2-2}
$$

$$
\vartheta_{V,mech,m} \quad \text{(도표 3-3, 3-4)}
$$



## 🔹공조기 최대 가열성능


$$
Q_H^* = \dot{V}^* \, \rho_L \cdot \left( h_{ZUL,W} - h_{AUL,W} - \Delta h_{WRG} \right) / 3600 \quad \text{[kW]} \tag{3-57} \quad \text{증기가습 있을 경우}
$$

$$
Q_H^* = \dot{V}^* \, \rho_L \cdot \left( c_{p,L} \left( \vartheta_{ZUL,W} - \vartheta_{AUL,W} \right) - \Delta h_{WRG} \right) / 3600 \quad \text{[kW]} \tag{3-58} \quad \text{증기가습 없을 경우}
$$

$$
\rho_L = 1.204 \, \mathrm{kg/m^3}, \quad c_{p,L} = 1.006 \, \mathrm{kJ/(kg \cdot K)}
$$

$$
\dot{V}^* = \dot{V}_{mech.m}
$$

### 습도요구 조건에 따른 $h_{ZUL,W}$ 계산식

- 습도요구 없음 (3-38):

$$
h_{ZUL,W} = 1.01 \, \vartheta_{ZUL,W} + 0.001 \left(2501 + 1.86 \, \vartheta_{ZUL,W} \right)
$$

- 편차가 있는 습도요구 (3-42):

$$
h_{ZUL,W} = 1.01 \, \vartheta_{ZUL,W} + 0.006 \left(2501 + 1.86 \, \vartheta_{ZUL,W} \right)
$$

- 편차가 없는 습도요구 (3-48):

$$
h_{ZUL,W} = 1.01 \, \vartheta_{ZUL,W} + 0.008 \left(2501 + 1.86 \, \vartheta_{ZUL,W} \right)
$$

단위: $[kJ/kg]$

또한,

$$
\vartheta_{ZUL,W} = \vartheta_{h,mech.min} \quad \text{(도표 3-3)}
$$

$$
c_{p,L} = 1.006 \, \mathrm{kJ/(kg \cdot K)}
$$

### 열 회수기 열량 $\Delta h_{WRG}$ 계산

- 열 회수기 없음 (3-54):
$$
\Delta h_{WRG} = 0
$$

- 순수 현열 회수기 (3-55):
$$
\Delta h_{WRG} = \Phi_{WRG} \cdot c_{p,L} \left( \vartheta_{ABL,W} - \vartheta_{AUL,W} \right)
$$

- 현열 및 습기 회수기 (3-56):
$$
\Delta h_{WRG} = \Phi_{WRG} \cdot c_{p,L} \left( h_{ABL,W} - h_{AUL,W} \right)
$$

- 단위: $[\mathrm{kJ/kg}]$

- 관련 변수:
  - $\Phi_{WRG}$: 제품 사양에 따름
  - $h_{ABL,W}$: 도표 3-7
  - $\vartheta_{ABL,W}$: 도표 3-7
  - $\vartheta_{AUL,W}$, $h_{AUL,W}$: 도표 3-6



## 🔹공조기 최대 냉각성능


- 최대 냉각성능 계산식 (3-52):

$$
Q_C^* = \dot{V}^* \cdot \rho_L \cdot \left( h_{ZUL,Z} - h_{ABL,Z} - \Delta h_{WRG} \right) / 3600 \quad [\mathrm{kW}]
$$

- 기본값:
$$
\rho_L = 1.204 \, \mathrm{kg/m^3} \quad c_{p,L} = 1.006 \, \mathrm{kJ/(kg \cdot K)}
$$

- 열회수량 $\Delta h_{WRG}$ 정의:
- 열회수기 **없음** (3-59):
$$
\Delta h_{WRG} = 0
$$
- **순수 현열 회수기** (3-55):
$$
\Delta h_{WRG} = \Phi_{WRG} \cdot c_{p,L} \cdot (\vartheta_{ABL,Z} - \vartheta_{ZUL,Z})
$$
- **현열 및 습기 회수기** (3-56):
$$
\Delta h_{WRG} = \Phi_{WRG} \cdot (h_{ABL,Z} - h_{ZUL,Z})
$$

---

### 공급공기 엔탈피 계산 (조건별 선택)

- (3-38) 습도 요구 없음:
$$
h_{ZUL,Z} = 1.01 \vartheta_{ZUL,Z} + 0.012 (2501 + 1.86 \vartheta_{ZUL,Z}) \quad \text{if } p_s(\vartheta_{ZUL,Z}) > 1892 \, \mathrm{Pa}
$$

- (3-39) 습도 요구 없음 (정정):
$$
h_{ZUL,Z} = 1.01 \vartheta_{ZUL,Z} + x_{ZUL,Z} (2501 + 1.86 \vartheta_{ZUL,Z}) \quad \text{if } p_s(\vartheta_{ZUL,Z}) \leq 1892 \, \mathrm{Pa}
$$

- (3-40) 전차가 있는 습도 요구:
$$
h_{ZUL,Z} = 1.01 \vartheta_{ZUL,Z} + 0.011 (2501 + 1.86 \vartheta_{ZUL,Z}) \quad \text{if } p_s(\vartheta_{ZUL,Z}) > 1373 \, \mathrm{Pa}
$$

- (3-43) 전차가 있는 습도 요구 (정정):
$$
h_{ZUL,Z} = 1.01 \vartheta_{ZUL,Z} + x_{ZUL,Z} (2501 + 1.86 \vartheta_{ZUL,Z}) \quad \text{if } p_s(\vartheta_{ZUL,Z}) \leq 1373 \, \mathrm{Pa}
$$

- (3-48) 전차가 없는 습도 요구:
$$
h_{ZUL,Z} = 1.01 \vartheta_{ZUL,Z} + 0.008 (2501 + 1.86 \vartheta_{ZUL,Z}) \quad \text{if } p_s(\vartheta_{ZUL,Z}) > 1260 \, \mathrm{Pa}
$$

- (3-50) 전차가 없는 습도 요구 (정정):
$$
h_{ZUL,Z} = 1.01 \vartheta_{ZUL,Z} + x_{ZUL,Z} (2501 + 1.86 \vartheta_{ZUL,Z}) \quad \text{if } p_s(\vartheta_{ZUL,Z}) \leq 1260 \, \mathrm{Pa}
$$

---

### 습기함량 계산

- (3-41):
$$
x_{ZUL,Z} = \frac{0.5911}{\frac{100000}{p_s(\vartheta_{ZUL,Z})} - 0.95}
$$

- (3-37) 포화수증기압 공식:
$$
p_s(\vartheta) = \frac{28.021 - \frac{4006}{\vartheta + 236.7}}{1}
\quad \text{단, } 0.01^\circ C \leq \vartheta \leq 50^\circ C
$$

---

### 공급공기온도 하한

- (도표 3-3 참조):
$$
\vartheta_{ZUL,Z} = \vartheta_{h,mech.min}
$$



## 🔹공조기 최대 가습성능


$$
Q_{St}^* = \dot{V}^* \cdot \rho_L \cdot \left( h_{ZUL,W} - h_{AUL,W} - \Delta h_{WRG} \right) / 3600 \quad [\text{kW}] \tag{3-65}
$$

### 습공급 후 온도별 엔탈피 수식 정리

- **습도요구 없음** (3-38):

$$
h_{ZUL,W} = 1.01 \vartheta_{ZUL,W} + 0.001 \left(2501 + 1.86 \vartheta_{ZUL,W} \right)
$$

- **편차가 있는 습도요구** (3-42):

$$
h_{ZUL,W} = 1.01 \vartheta_{ZUL,W} + 0.006 \left(2501 + 1.86 \vartheta_{ZUL,W} \right)
$$

- **편차가 없는 습도요구** (3-48):

$$
h_{ZUL,W} = 1.01 \vartheta_{ZUL,W} + 0.008 \left(2501 + 1.86 \vartheta_{ZUL,W} \right)
$$

### 열 회수기 수식 정리

- **열 회수기 없음** (3-63):

$$
\Delta h_{WRG} = 0
$$

- **현열 및 습기 회수기** (3-64):

$$
\Delta h_{WRG} = 2501 \, \Phi_{WRG} \left( x_{ABL,W} - x_{AUL,W} \right)
$$

### 열 회수식 관련 변수 출처

- $\Phi_{WRG}$ : 제품 사양에 따라 주어지는 열 회수 효율
- $x_{ABL,W_i}$ : 공급 공기 절대습도 (표 3-7 참고)
- $x_{AUL,W_i}$ : 외기 절대습도 (표 3-6 참고)
