import asyncio
import os

import anchorpy
from solana.rpc.commitment import Confirmed

from zetamarkets_py.client import Client


async def main():
    # Get local filesystem keypair wallet, defaults to ~/.config/solana/id.json
    wallet = anchorpy.Wallet.local()
    commitment = Confirmed
    endpoint = os.getenv("ENDPOINT", "https://api.mainnet-beta.solana.com")
    ws_endpoint = os.getenv("WS_ENDPOINT", "wss://api.mainnet-beta.solana.com")

    # Load in client without any markets
    client = await Client.load(
        endpoint=endpoint, ws_endpoint=ws_endpoint, commitment=commitment, wallet=wallet, assets=[]
    )

    # Subscribe to margin account events
    print(f"Listening for events on margin account: {client._margin_account_address}")
    async for tx_events in client.subscribe_events():
        # Loop over the events in each tx
        for event in tx_events:
            # Event can be PlaceOrder, Trade, OrderComplete or Liquidate
            print(event)


asyncio.run(main())
