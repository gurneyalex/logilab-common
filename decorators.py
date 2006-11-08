# Copyright (c) 2006 LOGILAB S.A. (Paris, FRANCE).
# http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
"""this module contains some function/method decorators"""

# XXX rewrite so we can use the decorator syntax when keyarg has to be specified

def cached(callableobj, keyarg=None):
    """simple decorator to cache result of method call"""
    #print callableobj, keyarg, callableobj.func_code.co_argcount
    if callableobj.func_code.co_argcount == 1 or keyarg == 0:
        
        def cache_wrapper1(self, *args):
            cache = '_%s_cache_' % callableobj.__name__
            #print 'cache1?', cache
            try:
                return getattr(self, cache)
            except AttributeError:
                #print 'miss'
                value = callableobj(self, *args)
                setattr(self, cache, value)
                return value
        return cache_wrapper1
    
    elif keyarg:
        
        def cache_wrapper2(self, *args, **kwargs):
            cache = '_%s_cache_' % callableobj.__name__
            key = args[keyarg-1]
            #print 'cache2?', cache, self, key
            try:
                _cache = getattr(self, cache)
            except AttributeError:
                #print 'init'
                _cache = {}
                setattr(self, cache, _cache)
            try:
                return _cache[key]
            except KeyError:
                #print 'miss', self, cache, key
                _cache[key] = callableobj(self, *args, **kwargs)
            return _cache[key]
        return cache_wrapper2
    def cache_wrapper3(self, *args):
        cache = '_%s_cache_' % callableobj.__name__
        #print 'cache3?', cache, self, args
        try:
            _cache = getattr(self, cache)
        except AttributeError:
            #print 'init'
            _cache = {}
            setattr(self, cache, _cache)
        try:
            return _cache[args]
        except KeyError:
            #print 'miss'
            _cache[args] = callableobj(self, *args)
        return _cache[args]
    return cache_wrapper3

def clear_cache(obj, funcname):
    """function to clear a cache handled by the cached decorator"""
    try:
        delattr(obj, '_%s_cache_' % funcname)
    except AttributeError:
        pass

def copy_cache(obj, funcname, cacheobj):
    """copy cache for <funcname> from cacheobj to obj"""
    cache = '_%s_cache_' % funcname
    try:
        setattr(obj, cache, getattr(cacheobj, cache))
    except AttributeError:
        pass


class wproperty(object):
    """simple descriptor expecting to take a modifier function as first argument
    and looking for a _<function name> to retreive the attribute
    """
    def __init__(self, setfunc):
        self.setfunc = setfunc
        self.attrname = '_%s' % setfunc.__name__
        
    def __set__(self, obj, value):
        setfunc(obj, value)
        
    def __get__(self, obj, cls):
        assert obj is not None
        return getattr(obj, self.attrname)
