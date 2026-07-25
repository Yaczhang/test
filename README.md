# 第一章与第二章终稿修订版

本分支按照以下边界完成修订：

- 第一章中的“现有研究不足与本文研究思路”和“本文主要研究内容与章节安排”保持原文冻结，待主要工作章节完成后再与摘要、结论与展望统一确认。
- 第二章图2.1至图2.3按照本轮要求保持原文件不变，不纳入本轮图件修改。
- 第一章其余正文和图题、第二章除图2.1至图2.3之外的正文、公式、符号、表格、图2.4和评价指标均已重新审查并修订。

## 文件

- `chapters/chap01_final.tex`
- `chapters/chap02_final.tex`
- `figures/chap02/fig2_01_two_models_final.tex`，本轮保持不变
- `figures/chap02/fig2_02_multiphysics_domains_final.tex`，本轮保持不变
- `figures/chap02/fig2_03_ale_mesh_final.tex`，本轮保持不变
- `figures/chap02/fig2_04_observation_inverse_framework_final.tex`，本轮已修订
- `FINAL_REVISION_REPORT.md`

第一章继续调用原工程中的三幅文献图：

- `figures/chap01/fig_rtdc_mietke2015.png`
- `figures/chap01/fig_rtdc_mokbel2017.png`
- `figures/chap01/fig_drop_impact_pasandideh1996.png`

## 第一章修订内容

- 保持两个冻结小节逐字不变。
- 删除非冻结部分中过早展开的本文具体任务安排，强化研究背景与研究进展主线。
- 规范“质谱流式细胞术”“基于液滴条形码的单细胞转录组测序”等术语。
- 将实时变形细胞术的加载机制统一表述为微通道内水动力应力。
- 统一使用“含细胞复合液滴”“圆度偏差”和“黏弹性特征时间”等术语。
- 合并重复的限制性说明，减少解释性和防御性语气。
- 第一章三幅文献图的图题统一标明“引自文献”。

## 第二章修订内容

- 保持统一物理和数值框架，不将两个数值模型机械拆分。
- 将材料参数明确为正问题输入和过程级标签，不再表述为求解器输出。
- 删除第二章中重复写入的微通道细胞膜具体厚度，具体参数由第三章给出。
- 莫尼里夫林模型只保留一般理论关系，第三章特定材料标签换算由第三章说明。
- 黏弹性参数关系采用 `eta_s = E tau_v`，与当前第四章可封存版本一致。
- 点坐标处理采用原始样本文件中的固定变换 `N_coord`，不补写未保存的物理参考长度。
- 将动态接触角统一称为“名义动态接触角”，删除未被原始记录保存的拟合窗口和采样点数。
- 补充内部细胞外表面的固定相场润湿边界说明。
- 右柯西格林张量记为 `C_CG`，圆度记为 `mathcal C`，内部细胞初始直径记为 `d_s,0`，减少符号复用。
- 补充 MRE@95%、半径百分比误差、几何量绝对误差和相对误差公式。
- 图2.4改为离线样本生成和在线参数反演两个阶段，明确材料参数在两个阶段中的不同角色。

## 参考文献

章节引用键继续对应用户现有的 `参考文献数据库_前四章_可封存终稿完成版.bib`。主工程只加载一份统一数据库，避免重复引用键。

当前修订未批量重命名现有引用键，以免影响第三章和第四章。参考文献显示年份由条目中的 `year` 字段决定，键名仅用于工程内部索引。

## 跨章节一致性检查

已核对当前可封存第三章和第四章对第二章公式标签的调用。以下标签在第二章修订版中继续保留：

- `eq:ch2_fourier_contour`
- `eq:ch2_mooney_rivlin`
- `eq:ch2_mr_modulus_relation`
- `eq:ch2_fourier_vector`
- `eq:ch2_vae_reparameterization`
- `eq:ch2_vae_kl`
- `eq:ch2_attention`
- `eq:ch2_circularity_deviation`
- `eq:ch2_centroid_velocity`
- `eq:ch2_smooth_l1_vector`
- `eq:ch2_volume_fraction`
- `eq:ch2_kelvin_voigt_time`
- `eq:ch2_phase_mobility`

## 最终集成检查

合并至上海大学学位论文主工程后，需要执行一次干净编译，并检查：

- 第一章三幅图片是否位于规定路径
- 图2.1至图2.3后续重绘文件是否保持原文件名和标签
- 表格是否超出版心
- 公式和图表浮动位置
- 第三章和第四章对第二章公式标签的调用
- 全文符号表中的 `varphi`、`psi`、`mathcal C`、`D_c`、`tau_v` 和 `eta_s`
- 两个冻结小节是否保持原文不变
