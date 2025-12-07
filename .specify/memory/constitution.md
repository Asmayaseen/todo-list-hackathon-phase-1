<!--
Sync Impact Report:
Version: 0.0.0 → 1.0.0 (Initial constitution creation)
Modified Principles: N/A (new)
Added Sections: All 5 core principles + Governance
Removed Sections: None
Templates Requiring Updates: ✅ All templates will inherit these principles
Follow-up TODOs: None
-->

# LifeStepsAI | Todo In-Memory Python Console App Constitution

## Core Principles

### I. Methodology: Spec-Driven & Test-Driven Development (NON-NEGOTIABLE)

**Spec-Driven Development (SDD) MUST be followed**
- All development MUST strictly adhere to Spec-Driven Development (SDD) principles
- Every feature MUST have a corresponding specification file in `/specs/features/` before implementation
- Specifications MUST include:
  - User stories ("As a user, I can...")
  - Acceptance criteria (clear, testable requirements)
  - Edge cases and error scenarios
  - Expected behavior with examples
- NO code may be written without an approved specification

**Test-Driven Development (TDD) is MANDATORY**
- The Test-Driven Development (TDD) pattern MUST be followed for all implementations
- Tests MUST be written BEFORE implementation code (Red-Green-Refactor cycle)
- Development cycle:
  1. **RED**: Write a failing test that describes expected behavior
  2. **GREEN**: Write minimal code to make the test pass
  3. **REFACTOR**: Improve code quality without changing behavior
- Every test MUST test one specific behavior or edge case
- Test names MUST clearly describe what they test (e.g., `test_add_task_with_valid_title_succeeds`)

**Rationale**: Spec-driven development ensures clarity before coding. TDD ensures correctness, prevents regressions, and creates living documentation. These practices are foundational for maintainable software.

### II. Code Quality: Clean Code with Type Hints & Docstrings (NON-NEGOTIABLE)

**Clean Code Principles MUST be followed**
- All code MUST adhere to clean code principles:
  - Meaningful, descriptive variable and function names
  - Single Responsibility Principle (one function = one purpose)
  - Functions MUST be small (ideally < 20 lines)
  - DRY (Don't Repeat Yourself) - no code duplication
  - Well-structured modules with clear separation of concerns
- Code MUST be self-documenting through clear naming
- Magic numbers MUST be replaced with named constants

**Type Hints are REQUIRED**
- All function signatures MUST include explicit Python type hints (PEP 484)
- Type hints MUST cover:
  - Function parameters
  - Return types
  - Class attributes where beneficial
- Example:
  ```python
  def add_task(title: str, description: str = "") -> Task:
      """Add a new task to the list."""
      pass
  ```

**Docstrings are MANDATORY for Public Functions**
- All public functions and classes MUST have clear docstrings
- Docstrings MUST explain:
  - Purpose (what the function does)
  - Parameters (what inputs it expects)
  - Return values (what it returns)
  - Exceptions raised (what errors can occur)
- Follow Google or NumPy docstring style

**Python Project Structure is REQUIRED**
- Proper Python project structure MUST be followed:
  - `/src/todo_app/` - Application source code
  - `/tests/` - Unit tests (mirrors src structure)
  - `pyproject.toml` - Project configuration (UV)
  - `README.md` - Setup and usage documentation
  - `CLAUDE.md` - Claude Code instructions

**Rationale**: Clean code with type hints and docstrings improves readability, maintainability, and enables IDE autocompletion. Clear structure makes collaboration easier.

### III. Testing: 100% Unit Test Coverage for Core Logic (NON-NEGOTIABLE)

**Test Coverage Target: 100%**
- A 100% unit test coverage target is MANDATED for all core business logic
- Core logic includes:
  - Task model operations
  - TodoManager CRUD operations
  - Input validation logic
  - Error handling paths
- UI/Console interface may have lower coverage (focus on core logic)

**Every Operation MUST be Tested**
- Every documented feature MUST have corresponding tests
- Every edge case identified in specs MUST have a test
- Tests MUST cover:
  - Happy path (normal operation)
  - Edge cases (empty inputs, boundary conditions)
  - Error cases (invalid inputs, constraints violations)
  - State changes (data modifications)

**Test Quality Standards**
- Tests MUST be independent (no interdependencies)
- Tests MUST be repeatable (same input → same output)
- Tests MUST be fast (unit tests complete in milliseconds)
- Test names MUST be descriptive (e.g., `test_delete_nonexistent_task_raises_error`)
- Use pytest framework with fixtures for reusable test setup

**Rationale**: 100% coverage ensures reliability and maintainability. Every operation is verified, preventing bugs and enabling confident refactoring.

### IV. Data Storage: Strictly In-Memory for Phase I (PHASE-SPECIFIC CONSTRAINT)

**No Persistent Storage Allowed**
- For Phase I implementation, ALL data storage MUST remain strictly in-memory
- NO persistent storage mechanisms are permitted:
  - ❌ No file system writes (JSON, CSV, pickle, etc.)
  - ❌ No databases (SQLite, PostgreSQL, etc.)
  - ❌ No external storage systems
- Data structures MUST use Python built-in types:
  - ✅ Lists, dictionaries, sets
  - ✅ In-memory objects (Task instances)
  - ✅ Class attributes for state

**Data Lifecycle**
- All task data lives only during application runtime
- Data is lost when application terminates (expected behavior)
- Each application run starts with empty task list

**Rationale**: In-memory constraint ensures rapid prototyping, simplifies initial architecture, and focuses learning on core logic rather than persistence mechanisms. Phase II will introduce persistent storage.

### V. Error Handling: Explicit Exceptions & Input Validation (NON-NEGOTIABLE)

**Explicit, Descriptive Exceptions REQUIRED**
- The use of explicit, descriptive exceptions is REQUIRED for all operational failures
- Custom exception classes MUST be created:
  - `TaskNotFoundException` - when task ID doesn't exist
  - `InvalidTaskDataError` - when task data is invalid
  - `DuplicateTaskError` - when task ID already exists (if applicable)
- Exception messages MUST be clear and actionable:
  - ❌ Bad: `"Error"`
  - ✅ Good: `"Task with ID 5 not found"`

**Input Validation is MANDATORY**
- All user input MUST be validated before processing
- Validation requirements:
  - Task IDs MUST be valid integers (raise `ValueError` for non-integers)
  - Task titles MUST NOT be empty (raise `InvalidTaskDataError`)
  - Task titles MUST be ≤ 200 characters
  - Task descriptions MUST be ≤ 1000 characters (if provided)
- Validation MUST happen at entry points (before business logic)

**Error Handling Standards**
- NEVER use bare `except:` clauses (always catch specific exceptions)
- Errors MUST be logged with context (what operation failed, why)
- User-facing error messages MUST be friendly and helpful
- Internal errors MUST preserve stack traces for debugging

**Rationale**: Explicit exceptions prevent silent failures and crashes. Input validation ensures data integrity and prevents system corruption. Clear error messages improve user experience.

## Development Workflow

**Quality Gates & Review Process**

1. **Spec-Driven Development**:
   - Write specification in `/specs/features/<feature-name>.md`
   - Get spec approval before coding
   - Reference spec in all related code

2. **Test-Driven Development**:
   - Write failing test first (RED)
   - Implement minimal code to pass (GREEN)
   - Refactor for quality (REFACTOR)
   - Repeat for each behavior

3. **Code Review Requirements**:
   - All code MUST be reviewed for:
     - Constitution compliance
     - Test coverage
     - Type hints and docstrings
     - Clean code principles

4. **Testing Gates**:
   - All tests MUST pass before commit
   - Coverage MUST be 100% for core logic
   - No failing tests allowed in main branch

## Governance

**Constitution Authority & Amendment Process**

This constitution supersedes all other development practices and guidelines. All code submissions MUST comply with these principles.

**Amendment Requirements**:
1. Amendments MUST be documented with rationale
2. Breaking changes MUST include migration plan
3. Version MUST be incremented according to semantic versioning:
   - MAJOR: Backward incompatible principle changes
   - MINOR: New principles or material expansions
   - PATCH: Clarifications, wording improvements

**Compliance Verification**:
- All code reviews MUST verify constitution compliance
- Non-compliant code MUST NOT be merged
- Deviations MUST be justified with documented rationale

**Enforcement**:
- Tests MUST pass (100% for core logic)
- Type hints MUST be present on all public functions
- Docstrings MUST be present on all public functions
- In-memory storage constraint MUST be maintained (Phase I)
- Spec-Driven and Test-Driven Development MUST be followed

**Phase-Specific Notes**:
- Phase I specifically mandates in-memory storage with no persistent data mechanisms
- Future phases (II-V) will introduce persistent storage, web interfaces, AI integration, and cloud deployment
- This constitution will be updated for each phase with phase-specific constraints

**Version**: 1.0.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07
