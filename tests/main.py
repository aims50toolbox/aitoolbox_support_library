import sys
sys.path.insert(0, '../src')

import logging
import asyncio
import tornado
import json
import argparse
import aitoolbox_support_lib.context as aictx
import aitoolbox_support_lib.sources as aisources
import aitoolbox_support_lib.errors as aierr


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        context = aictx.ServerContext()
        aictx.Context.set(context)

        logging.info('Got request')
        logging.debug(f'Headers: {self.request.headers}')

        context.set_sources(aisources.RESTSources(self.request))
        
        print("Sources:")
        print(context.get_sources())
        print()

        context.get_destinations().enable_single_mimetype(True)
        for k,v in context.get_sources().to_dict().items():
            context.get_destinations().set(k,v)

        context.get_destinations().generate_response(self)


async def main():
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])

    app.listen(args.port)
    logging.info(f"Server started on port {args.port}")
    await asyncio.Event().wait()

if __name__ == "__main__":
    logging.basicConfig(level = logging.DEBUG)

    parser = argparse.ArgumentParser(description='LLM server')
    parser.add_argument('--port', metavar='p', type=int, default=8080,
                    help='the server port number (default: 80)')
    args = parser.parse_args()

    asyncio.run(main())