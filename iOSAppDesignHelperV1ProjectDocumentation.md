# iOS App Design Helper v1 — Project Documentation

**Project:** Creation of a custom Grok skill for multi-platform SwiftUI app development  
**Skill Name:** `swiftui-multiplatform-development`  
**Created:** June 14, 2026  
**Version:** v1 (Initial Release)  
**Author:** Grok (with user Nathan Rossow)  
**Location:** `/home/workdir/.grok/skills/swiftui-multiplatform-development/`

---

## 1. Project Goal

The user requested a specialized skill to help with **writing iOS apps** that work across:

- iPhone
- iPad (tablet)
- Mac (laptop and desktop)

The goal was to create a reusable, high-quality instruction set that Grok can load when the user needs help designing, architecting, or implementing SwiftUI applications for the full Apple ecosystem.

This skill focuses on **modern, production-ready practices** rather than basic syntax the model already knows.

---

## 2. Why a Custom Skill Was Needed

While Grok has strong general knowledge of Swift and SwiftUI, a dedicated skill provides:

- Structured decision frameworks (architecture, data layer, UI patterns)
- Current 2026-era recommendations (Swift 6, Observation framework, SwiftData)
- Consistent guidance across multi-platform challenges
- Emphasis on maintainability for solo developers or small business tool projects
- Specific anti-patterns and pitfalls to avoid

---

## 3. Step-by-Step Creation Process

### Step 1: User Request for Tutorial
- User asked: `skill-creator skill tutorial`
- I read the official `skill-creator` documentation from `/root/.grok/skills/skill-creator/SKILL.md`
- Provided a clear tutorial explaining how skills work, the required format, and the creation workflow

### Step 2: User Confirmed Skill Creation
- User responded:  
  > "Yes. I want to create a specific skill for writing iOS apps for iphones and laptop and desktop and tablet iOS softwares."

### Step 3: Skill Initialization
I used the official init script to bootstrap the skill:

```bash
bash /root/.grok/skills/skill-creator/scripts/init-skill.sh \
  swiftui-multiplatform-development \
  /home/workdir/.grok/skills \
  --resources references
```

**Result:**
- Created directory: `/home/workdir/.grok/skills/swiftui-multiplatform-development/`
- Generated template `SKILL.md`
- Created empty `references/` folder

### Step 4: Writing the SKILL.md
I replaced the template with a comprehensive, production-focused instruction set covering:

- Core principles for 2026-era development
- Project setup and multi-target configuration
- Architecture recommendations (MV + Observation, when to consider TCA)
- Adaptive interface patterns (`NavigationSplitView`, size classes)
- Data persistence with **SwiftData** (preferred)
- Networking, concurrency, and state management
- Widgets, App Intents, and system integration
- Testing, performance, and deployment workflows
- Common pitfalls and iteration guidance

The instructions are written in **imperative form** and focus on what the model should *do* when helping the user.

### Step 5: Validation
Ran the official validator:

```bash
bash /root/.grok/skills/skill-creator/scripts/validate-skill.sh \
  /home/workdir/.grok/skills/swiftui-multiplatform-development
```

**Result:** `OK: Skill 'swiftui-multiplatform-development' is valid (118 lines)`

---

## 4. Final Skill Structure

```
swiftui-multiplatform-development/
├── SKILL.md                          # Core instructions (118 lines)
└── references/
    └── iOS-app-design-helper-v1-project.md   # This document
```

---

## 5. Full Content of SKILL.md (v1)

```markdown
---
name: swiftui-multiplatform-development
description: Use this skill when the user wants to design, architect, or implement SwiftUI apps targeting iPhone, iPad, and Mac. Apply it for multi-platform projects, adaptive interfaces, modern data handling, architecture decisions, deployment workflows, and production best practices across Apple devices.
---

# SwiftUI Multiplatform Development

## Overview

This skill provides structured guidance for building high-quality SwiftUI applications that run natively on iPhone, iPad, and Mac (via Mac Catalyst or native targets). It emphasizes current 2026-era patterns using Swift 6, the Observation framework, SwiftData, and adaptive UI techniques that scale cleanly across form factors.

## Core Principles

- Prefer SwiftUI for new projects unless a specific UIKit component or legacy requirement exists.
- Design for the smallest supported device first, then expand using size classes, NavigationSplitView, and platform-specific modifiers.
- Use Swift 6 strict concurrency and the Observation framework (`@Observable`) instead of legacy Combine-heavy patterns where possible.
- Choose SwiftData for new persistence layers; fall back to Core Data only when advanced migration or CloudKit sharing features are required.
- Keep business logic in plain Swift types (services, repositories, use cases) and let SwiftUI views observe state.

## Project Setup and Targets

- Create a single Xcode project with multiple targets or use a multi-platform app template.
- Enable Mac Catalyst early if targeting Mac, or create a native Mac target for better performance and deeper integration.
- Use Swift Package Manager for internal modules and third-party dependencies.
- Configure Info.plist capabilities (network, background modes, iCloud, etc.) per platform thoughtfully — do not enable everything everywhere.
- Set minimum deployment targets realistically (iOS 17+ / macOS 14+ recommended in 2026 for modern SwiftUI features).

## Architecture Recommendations

- For most apps: Simple MV pattern with `@Observable` model objects + `@State` / `@Environment` in views.
- For complex apps with many features: Consider The Composable Architecture (TCA) or a lightweight custom coordinator pattern.
- Separate concerns clearly:
  - Views: Pure presentation and user interaction
  - ViewModels / Observable Models: State and business rules
  - Services / Repositories: Data access, networking, persistence
- Use dependency injection (simple initializers or environment values) rather than singletons.
- Prefer value types (`struct`) for models and use `@Observable` classes only when mutation and observation are needed.

## Building Adaptive Interfaces

- Use `NavigationSplitView` for iPad and Mac sidebar layouts; fall back gracefully on iPhone with `NavigationStack`.
- Leverage `.regular` / `.compact` size classes and `horizontalSizeClass` / `verticalSizeClass` environment values.
- Apply platform modifiers: `.platform()` or `#if os(iOS)` / `#if os(macOS)` sparingly — prefer cross-platform solutions first.
- Use `GeometryReader` and custom layout containers only when SwiftUI's built-in responsive tools are insufficient.
- Test layouts continuously in Xcode Previews across all device sizes and orientations.
- Support Dynamic Type and accessibility from the first screen — use scalable fonts and semantic elements.

## Data and Persistence

- Default to **SwiftData** for new apps. It integrates cleanly with SwiftUI and Observation.
- Use `@Query` and `@Environment(\.modelContext)` for data access in views.
- For syncing across devices, enable CloudKit with SwiftData (or NSPersistentCloudKitContainer if using Core Data).
- Implement proper model versioning and lightweight migrations from day one.
- Cache network responses intelligently and provide offline-first experiences where appropriate.
- Handle large datasets with pagination or cursor-based loading rather than loading everything into memory.

## Networking and Concurrency

- Use `async`/`await` and structured concurrency everywhere.
- Wrap network calls in repository-style services that return domain types, not raw JSON.
- Handle errors explicitly with typed error models rather than generic `Error`.
- Use `URLSession` with modern configuration (`.default`, background sessions when needed).
- For real-time features, evaluate WebSockets or Apple's Push Notifications + CloudKit.

## State Management and Observation

- Prefer the new Observation framework over `ObservableObject` + `@Published` for simpler code.
- Use `@State` for local view state and `@Environment` for shared values.
- For complex shared state, introduce a small number of observable model objects at the app or scene level.
- Avoid over-observation — only views that actually read a property should re-render.

## Widgets, App Intents, and System Integration

- Add WidgetKit extensions early if the app benefits from home screen or lock screen presence.
- Implement App Intents for Siri, Shortcuts, and Spotlight to improve discoverability.
- Use Live Activities for time-sensitive information when relevant.
- Support App Shortcuts and Spotlight indexing for better user experience on all platforms.

## Testing and Quality

- Write unit tests for business logic and repositories (not UI).
- Use Xcode Previews extensively for UI iteration — create multiple preview providers for different states and devices.
- Add UI tests with `XCUIApplication` for critical user flows.
- Profile performance with Instruments, especially on older devices and Mac.
- Test on physical devices regularly — simulators do not catch all Mac Catalyst or iPad-specific behaviors.

## Deployment and Distribution

- Manage signing and provisioning profiles carefully; use automatic signing where possible and manual for complex setups.
- Use TestFlight for internal and external testing on all platforms.
- For Mac apps: Decide between Mac App Store distribution vs. direct distribution (Developer ID + notarization).
- Configure App Store Connect metadata, screenshots, and privacy labels per platform.
- Implement phased releases and monitor crash reports via Xcode Organizer or third-party tools.
- Keep build numbers and marketing versions synchronized across targets.

## Common Pitfalls to Avoid

- Overusing platform-specific code early — it creates maintenance burden.
- Ignoring size classes and building iPhone-first UIs that break on iPad/Mac.
- Storing mutable state in views instead of observable models.
- Using Core Data when SwiftData would suffice.
- Neglecting accessibility, Dynamic Type, and right-to-left language support.
- Performing heavy work on the main actor — offload to background tasks or actors.
- Hardcoding colors, fonts, and spacing instead of using semantic tokens and design system values.

## Iteration Guidance

When helping with a specific feature or screen:
1. Clarify the target platforms and minimum OS versions.
2. Identify the data model and persistence needs.
3. Choose the simplest architecture that will scale.
4. Design the adaptive navigation and layout structure first.
5. Implement core functionality with clean separation of concerns.
6. Add polish: accessibility, animations, error handling, and offline support.
7. Test across devices in Previews and on hardware.
8. Prepare deployment configuration early.

Always prefer simple, maintainable solutions over clever or overly abstract ones. Revisit architecture only when complexity clearly justifies it.
```

---

## 6. How to Use the Skill

Once loaded, the skill activates when the user asks for help with:

- Designing multi-platform SwiftUI app architecture
- Building adaptive interfaces for iPhone + iPad + Mac
- Choosing between SwiftData / Core Data / CloudKit
- State management with modern Observation framework
- Deployment, TestFlight, and App Store processes across platforms
- Performance, accessibility, and maintainability best practices

**Example triggers:**
- “Using the swiftui skill, help me design a repair tracking app…”
- “Create a SwiftUI dashboard that works on iPhone, iPad, and Mac”
- “What architecture should I use for a multi-platform business tool?”

---

## 7. Future Improvements (v2 Ideas)

Potential enhancements for future versions:

- Add `references/architecture-patterns.md` with concrete code examples
- Add `references/multiplatform-gotchas.md` (common bugs and fixes)
- Add `references/deployment-checklist.md`
- Create `scripts/` for generating common project templates or boilerplate
- Add support for visionOS and tvOS if user needs expand
- Create companion skills (e.g., `swiftui-business-tools` for quoting/inventory apps)

---

## 8. Summary

This v1 skill gives Grok a focused, high-signal instruction set for helping build professional SwiftUI applications across Apple’s ecosystem. It was created following the official `skill-creator` workflow, validated, and is ready for immediate use.

The skill prioritizes **clarity, maintainability, and modern Apple-recommended patterns** — especially useful for building internal business tools, repair management apps, quoting systems, or client-facing applications.

---

**End of Project Documentation — iOS App Design Helper v1**
