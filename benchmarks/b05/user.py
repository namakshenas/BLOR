user_query = """
# Purchase Order Approval Process

## Overview

The Purchase Order Approval Workflow is designed to ensure proper authorization and budget compliance for all company purchases. This process begins when an employee identifies a business need requiring the procurement of goods or services and continues through various approval stages until a purchase order is issued to the vendor.

## Process Description

When an employee (the **Requester**) identifies a need to purchase goods or services, they initiate the process by completing a comprehensive purchase requisition form. This form captures essential information including a detailed description of the items needed, estimated costs, business justification for the purchase, the appropriate budget code, and any preferred vendors they may have identified. The requester submits this form electronically through the company's procurement system.

Once submitted, the request is routed to the requester's **Department Manager** for initial review. The manager examines the request to determine whether it aligns with departmental goals and represents a legitimate business need. At this critical decision point, the manager must decide whether the request is justified and falls within the department's scope of operations. If the manager determines the request lacks proper justification or falls outside the department's scope, they return it to the requester with detailed feedback explaining the concerns, and the process terminates. However, if the manager approves the request, it advances to the next stage.

The approved request then moves to the **Finance Controller**, who conducts a thorough budget verification. The controller checks whether sufficient funds are available in the designated budget code and confirms that the expense is properly allocated according to company financial policies. This represents another critical decision point: if the budget is unavailable or the allocation is improper, the request is returned to the requester with an explanation, ending the process. If budget availability is confirmed, the request proceeds forward.

At this stage, the system automatically evaluates the total purchase value to determine the appropriate approval pathway. For purchases under $5,000, the request proceeds directly to procurement. For purchases between $5,000 and $25,000, additional approval from the Department Manager is required, with focus on the strategic fit and financial impact. For high-value purchases exceeding $25,000, the request must be escalated to the **CEO or designated Executive** for final authorization. These senior leaders evaluate the request's alignment with company strategy, potential return on investment, and overall financial impact before making their approval decision.

If the senior approval is denied at this stage, the request is returned to the requester with detailed reasoning, and the process concludes. Upon receiving final approval, the request is forwarded to a **Procurement Specialist**, who takes responsibility for creating the official purchase order, negotiating terms with vendors if necessary, and managing the transaction through to completion. The procurement specialist ensures all documentation is properly filed and notifies relevant parties when the order has been successfully placed."""