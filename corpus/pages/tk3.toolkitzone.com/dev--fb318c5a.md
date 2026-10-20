---
kind: page
id: "tk3.toolkitzone.com/tk3.toolkitzone.com/dev/?page=gen"
site: "tk3.toolkitzone.com"
title: "General Principles"
original_url: "http://tk3.toolkitzone.com/dev/?page=gen"
written: null
date_confidence: "unknown"
updated: null
captured: ["20060207132444", "20070519232059"]
author: null
repliers: []
authors: []
comments_present: 0
converter_version: "1"
source_captures:
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/dev__page_gen_amp_3BPHPSESSID_b297667ce25940a5838e114be0fcd1bd", captured: "20060207132444", sha256: "ac2187eaba61fe851034eaa30608c6b85c9c0dc2d02bef30f8a56fe99c45bad4", wayback_url: "https://web.archive.org/web/20060207132444/http://tk3.toolkitzone.com/dev/?page=gen&amp%3BPHPSESSID=b297667ce25940a5838e114be0fcd1bd"}
  - {path: "wayback/toolkitzone.com/tk3.toolkitzone.com/dev__page_gen", captured: "20070519232059", sha256: "153fb3498bb4fcd299eca2e705420b3beae89cdd96d6f76b20f45a01db64ed2f", wayback_url: "https://web.archive.org/web/20070519232059/http://tk3.toolkitzone.com/dev/?page=gen"}
---

# General Principles

All development paths, features and improvements to the Toolkit must be discussed and assessed by the development team before being implemented. This ensures that all decisions made are in the best interests of the Toolkit and that no single developer has more control over the direction of the TK than any other.
A developer wishing to make any features or improvements must formally propse them by starting a topic in the development forum stating their intentions and explaining how they would go about implementing them.
Development paths can be proposed but do not necessarily have to be begun immediately. As future planning of development paths progresses, paths can be proposed to begin only once others are completed. In this way, a definitive picture of development can be constructed with a clear path to its completion.
Informal posts can be made to start discussions and do not have to contain detailed plans, but such topics cannot directly lead to an implementation without an formal proposal.
Testers can also propose features and improvements, but developers must first assess their feasibility before they can be formally proposed. One or more developers must also be willing to undertake the proposals. No developer can be forced to work on a development path against their wishes (although developers should (in general) always be working on some aspect of the Toolkit).
All team members must respond to formal proposals, both to discuss them and to vote on them. Other developers must assess the feasibility of the proposal. A proposal will only go ahead if it attains the majority vote. Members who repeatedly fail to vote will be asked to leave the team. If a majority for is not attained, the development path is delayed until the proposal can be modified so that the majority will vote for.
Once a proposal has been agreed on, developers must maintain regular contact (either through the forum or instant messaging) to monitor the progress of the feature. The progress of each development path must be kept up to date in the relevant topic.
When developers produce a build and post it on the forum, all testers should download and test it, and provide feedback, even in the case where no problems are found (a "clean" report is as valuable as a bug report).
Bug fixes do not need to "proposed" or discussed except in cases where fixes require large amounts of alterations or restructuring. Records of bug fixes must be made in the dev team's bug tracker.
When proposing features or assessing feasibility, the following aspects should be considered:
- Compatibility or conflict with any other development path.
- Amount of rewriting or restructuring required to achieve it.
- Backwards compatibility if end-user aspects alter.
- Relevance/importance of feature (e.g., a new rpgcode command—can its task already be accomplished?)
- Likelihood of introducing bugs to the system.
Official releases should be proposed and discussed like features. When a majority of users are happy with the state of the Toolkit and no one has major concerns, a release will be made. This must include a period of exclusive testing where no changes (except bug fixes) are made to the source to prevent new problems being introduced and increase the chance for a successful release.
