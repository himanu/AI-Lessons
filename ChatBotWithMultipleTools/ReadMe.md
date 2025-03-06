# Customer Service Chatbot with Multiple Tools

This project implements an intelligent customer service chatbot powered by the Claude LLM model and integrated with various tools to handle customer queries efficiently.

## Overview

The chatbot is designed to provide quick and accurate responses to customer inquiries by leveraging:
- Claude LLM for natural language understanding and generation
- Direct integration with customer service tools and APIs
- Contextual awareness of customer data and order history

## Understanding Tools in LLM Context

Tools are specialized functions that extend the capabilities of Large Language Models (LLMs) by allowing them to:
- Access external data sources and APIs
- Perform specific actions in response to user requests
- Retrieve real-time information
- Execute operations on behalf of users

Think of tools as the chatbot's "hands and feet" - while the LLM provides the intelligence to understand requests, tools enable it to take concrete actions like looking up orders or canceling them.

## Integrated Tools
The chatbot leverages the following tools:

### `get_user`
- Purpose: Retrieves customer profile and account information
- Use case: When customer asks about their account details or needs verification
- Example: "Can you tell me my shipping address on file?"

### `get_order_by_id`
- Purpose: Looks up specific order details using order ID
- Use case: When customer inquires about a particular order
- Example: "What's the status of order #12345?"

### `get_customer_orders`
- Purpose: Fetches complete order history for a customer
- Use case: When customer wants to review past purchases
- Example: "Show me all my orders from last month"

### `cancel_order`
- Purpose: Processes order cancellation requests
- Use case: When customer wants to cancel an order
- Example: "I need to cancel my recent order"

## Technical Architecture

The system consists of:

1. Claude LLM as the core language model
   - Handles natural language understanding
   - Determines which tools to use based on user queries
   - Generates human-like responses

2. Tool Integration Layer
   - Manages connections to backend services
   - Handles API authentication and requests
   - Formats data for LLM consumption

3. Context Management System
   - Maintains conversation history
   - Tracks tool usage during interactions
   - Ensures coherent multi-turn conversations

## Example Interactions


