# make.fun 新闻图任务 — 准备记录（未提交）

账号：@hracococool-ai（GitHub hracococool-ai），0 参赛，没绑钱包。
任务：Sum up 24 November's world news in one image
Slug：news-image-20261124
链接：https://make.fun/bounty/news-image-20261124

## 规则（2026-11-24 14:29 查的公开 API，GET /api/competitions/news-image-20261124）

- 免费，entry_fee = null / $0.00
- 总奖金 $100，前 50 名分：第 1 名 $20，第 2 名 $12，第 3 名 $6，第 4–10 名各 $2，第 11–50 名各 $1.20
- 截止：2026-11-26 08:00 中国时间（2026-11-26T00:00:00Z）；结果 2026-12-10 出
- 已有 6009 个提交（查的时候），前 50 名中奖率约 0.8%，别当成稳赚
- 评分：AI 评委看图，两两对比选更好的一张，按胜率排名；评委没有新闻源，只看图本身
- 作品不是只交一张图，而是一个程序：main.py（Python 3.13）或 main.ts（Node 22）在仓库根目录，评分时在沙箱里跑两次，两次必须写出完全相同的字节到 /output/entry.png；不能联网
- 图片：PNG 或 JPEG，≤1 MiB，≤1024x1024
- 仓库要求：公开、归 hracococool-ai 所有、在比赛开始后创建（2026-11-24T00:00:00Z 之后）、带 OSI 许可证（MIT/Apache-2.0）、README 要带 3 个 make.fun 徽章、GitHub About 要设 homepage https://make.fun/bounty/news-image-20261124 和 topics makefun, ai-agents, bounties, growth
- 必须交 AI 对话记录打包（bundle，kit 的 CLI 生成）；handed_over_places = none，意思是“手工交上来的对话记录”排得上名但拿不到钱——只有 harness 实际记录的对话才算
- 每天最多 10 次提交，总共最多 20 次；截止前最后一次提交是最终作品；4 轮盲评，提交时看不到排名

## 挡住提交的事（红线，没动）

1. **没绑 Solana 钱包**：account_wallet 检查会失败。提交要钱包签名 entry_message + entry_signature，奖金也打到这个钱包。没创建钱包、没导入私钥、没生成密钥对。
2. 还没在 GitHub 上建仓库（要等钱包决定后再建，因为仓库要在比赛开始后创建，现在建还来得及）。
3. 还没下载 kit（下载 kit 要 API key，API key 要钱包签名登录才能拿）。

## 本地草稿（已做好，未提交）

目录：~/workspace/makefun/news-image-20261124/
- entry.png：1024x1024 PNG，约 121 KB，6 格新闻信息图（见下）
- make_image.py：生成 entry.png 的脚本（PIL，确定性）
- main.py：把 entry.png 复制到 /output/entry.png，已验证两次运行 sha256 完全相同
- README.md、LICENSE（MIT）

图片内容（英文，评委是 AI，看图本身）：
1. TECH — NVIDIA BRINGS BACK HUANG：黄仁勋复职，特朗普介入，美股大涨
2. WAR AT SEA — UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA：乌克兰称海无人艇在利比亚近海击沉俄舰
3. SPACE — NUCLEAR SPACE WEAPON FEAR：盟友警告俄罗斯可能下月发射核武卫星，北约称保卫太空
4. DISASTER — 24 KILLED IN INDONESIA FACTORY FIRE：印尼工厂火灾 24 人死亡
5. EUROPE — BOMB THREATS HIT GERMAN SCHOOLS：德国数百所学校收到炸弹威胁；丹麦拟禁学校手机
6. SPORT — 2031 WOMEN'S WORLD CUP HOSTS NAMED：美国、墨西哥、哥斯达黎加、牙买加办 2031 女足世界杯，英国办 2035

新闻来源（2026-11-24 新闻搜索，news 垂直）：The Japan Times、The Straits Times、Qatar Tribune、The Manila Times、光华日报。
其他当天值得备选的新闻：俄罗斯死亡人数黑客数据称近 50 万；联合国粮农机构警告战争让 730 万人断粮；美国多州起诉马斯克公司 Grok 生成色情图片；伊朗油轮在霍尔木兹海峡触雷起火。

## 提交步骤（钱包决定后）

1. Li 决定钱包方案：新建一个 Solana 钱包（只给 make.fun 用）或关联已有钱包——这是关键决定，涉及私钥保管。
2. 把钱包绑到 make.fun 账号（个人页 Link a wallet），用钱包签名拿 API key（af_ 开头，30 天有效）。
3. 下载 kit：GET /c/news-image-20261124/kit，用 kit 的 CLI。
4. 在 GitHub 上新建公开仓库（hracococool-ai 名下），把本地草稿文件放进去，README 按官方模板加 3 个徽章和推荐链接，设好 About，提交。
5. 用 kit 打包对话记录（bundle），检查 transcripts 通过（至少 5 个助手回合、30% 代码行是 agent 自己写的、文件至少被改过 2 次、时间在比赛窗口内）。
6. 提交：node cli/makefun.mjs submit --competition news-image-20261124 --repo-url … --commit … --title … --bundle … --keypair …，在 2026-11-26 08:00 前完成。
7. 等 2026-12-10 出结果；中了再走领奖流程（链上签名，手续费约 0.0025 SOL 级别，以实际为准）。
